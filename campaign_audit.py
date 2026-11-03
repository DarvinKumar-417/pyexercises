# campaign_audit.py
# Session 8 final exam: read an ad campaign export, compute CTR / CPA / ROAS,
# quiz the player on five questions, save the score to result.csv.
#
# TODO (student): rewrite every comment below in your own words.
# TODO (student): set CSV_FILE to your real file name.

import csv
import os
from datetime import date

CSV_FILE = "campaigns_B.csv"   # change X to your letter/number
RESULT_FILE = "result.csv"

# Possible header names for each field. The export's real names are unknown
# to me, so the program tries several and picks the first that matches.
ALIASES = {
    "name": ["campaign", "campaign_name", "campaign name", "name", "campagne"],
    "channel": ["channel", "canal", "platform", "source", "medium"],
    "impressions": ["impressions", "impr", "impression"],
    "clicks": ["clicks", "click"],
    "cost": ["cost", "cost (€)", "spend", "amount_spent", "amount spent", "cout", "coût"],
    "conversions": ["conversions", "conversion", "conv"],
    "revenue": ["revenue", "revenue (€)", "revenu", "sales", "income"],
}


def to_number(text):
    """Turn a cell like '11088,60' into 11088.6. Return None if empty or invalid."""
    if text is None:
        return None
    text = str(text).strip().replace("\u00a0", "").replace(" ", "")
    text = text.replace("€", "").replace("$", "")
    if text == "":
        return None
    if "," in text:
        # European format: dot = thousands separator, comma = decimal point
        text = text.replace(".", "").replace(",", ".")
    try:
        return float(text)
    except ValueError:
        return None


def find_columns(header):
    """Map each field (name, cost, ...) to the real column name in the file."""
    cleaned = {h.strip().lower(): h for h in header}
    mapping = {}
    for field, options in ALIASES.items():
        for option in options:
            if option in cleaned:
                mapping[field] = cleaned[option]
                break
        if field not in mapping:
            raise ValueError(
                f"Column for '{field}' not found. Columns in file: {header}"
            )
    return mapping


def read_campaigns(path):
    """Read the CSV and return a list of clean campaign dictionaries.
    Rows with an empty impressions cell are excluded."""
    # Try utf-8 first, then latin-1 (common for European exports)
    for encoding in ("utf-8-sig", "latin-1"):
        try:
            with open(path, newline="", encoding=encoding) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue

    lines = content.splitlines()
    first_line = lines[0] if lines else ""
    # European exports often use ; as delimiter
    delimiter = max([";", ",", "\t"], key=first_line.count)

    reader = csv.DictReader(lines, delimiter=delimiter)
    columns = find_columns(reader.fieldnames)

    campaigns = []
    for row in reader:
        impressions = to_number(row[columns["impressions"]])
        if impressions is None:
            continue  # rule 1: empty impressions -> excluded everywhere

        campaigns.append({
            "name": (row[columns["name"]] or "").strip(),
            "channel": (row[columns["channel"]] or "").strip(),
            "impressions": impressions,
            "clicks": to_number(row[columns["clicks"]]) or 0,
            "cost": to_number(row[columns["cost"]]) or 0,
            "conversions": to_number(row[columns["conversions"]]) or 0,
            "revenue": to_number(row[columns["revenue"]]) or 0,
        })
    return campaigns


def compute_metrics(campaigns):
    """Add ctr, cpa and roas to each campaign. Use None when not computable."""
    for c in campaigns:
        c["ctr"] = c["clicks"] / c["impressions"] if c["impressions"] > 0 else None
        # rule 2: zero conversions -> no CPA, but campaign stays elsewhere
        c["cpa"] = c["cost"] / c["conversions"] if c["conversions"] > 0 else None
        c["roas"] = c["revenue"] / c["cost"] if c["cost"] > 0 else None
    return campaigns


def compute_answers(campaigns):
    """Compute the five correct answers from the data."""
    with_ctr = [c for c in campaigns if c["ctr"] is not None]
    with_cpa = [c for c in campaigns if c["cpa"] is not None]

    best_ctr = max(with_ctr, key=lambda c: c["ctr"])["name"]
    worst_cpa = max(with_cpa, key=lambda c: c["cpa"])["name"]
    roas_count = sum(1 for c in campaigns if c["roas"] is not None and c["roas"] > 3)

    conv_by_channel = {}
    for c in campaigns:
        conv_by_channel[c["channel"]] = conv_by_channel.get(c["channel"], 0) + c["conversions"]
    top_channel = max(conv_by_channel, key=conv_by_channel.get)

    # Shown as a percentage (e.g. 2.35 means 2.35 %)
    avg_ctr = round(sum(c["ctr"] for c in with_ctr) / len(with_ctr) * 100, 2)

    return [best_ctr, worst_cpa, roas_count, top_channel, avg_ctr]


QUESTIONS = [
    ("Which campaign has the best CTR?", "text"),
    ("Which campaign has the highest CPA?", "text"),
    ("How many campaigns have a ROAS above 3?", "int"),
    ("Which channel generated the most conversions in total?", "text"),
    ("What is the average CTR across all campaigns, in %, rounded to 2 decimals?", "float"),
]


def ask_player(prompt, kind):
    """Ask one question and keep asking until the input is valid."""
    while True:
        raw = input(prompt + "\n> ").strip()
        try:
            if kind == "int":
                return int(raw)
            if kind == "float":
                return float(raw.replace(",", "."))
            if raw == "":
                raise ValueError
            return raw
        except ValueError:
            print("Invalid answer, try again.")


def is_correct(given, expected, kind):
    """Compare the player's answer with the correct one."""
    if kind == "text":
        return str(given).strip().lower() == str(expected).strip().lower()
    if kind == "int":
        return given == expected
    return abs(given - expected) < 0.01  # float, 2 decimals


def run_quiz(answers):
    """Run the five questions and return the score."""
    score = 0
    for i, (question, kind) in enumerate(QUESTIONS):
        given = ask_player(f"Q{i + 1}. {question}", kind)
        if is_correct(given, answers[i], kind):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The answer was: {answers[i]}\n")
    return score


def save_result(player, score):
    """Append player name, score and date to result.csv (header if new)."""
    is_new = not os.path.exists(RESULT_FILE)
    with open(RESULT_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["player", "score", "date"])
        writer.writerow([player, score, date.today().isoformat()])


def main():
    step = "reading the CSV"
    try:
        campaigns = read_campaigns(CSV_FILE)
        step = "computing metrics"
        campaigns = compute_metrics(campaigns)
        step = "computing answers"
        answers = compute_answers(campaigns)

        step = "running the quiz"
        player = input("Player name: ").strip() or "Anonymous"
        score = run_quiz(answers)
        print(f"Final score: {score}/{len(QUESTIONS)}")

        step = "saving the result"
        save_result(player, score)
    except FileNotFoundError:
        print(f"Error while {step}: file not found ({CSV_FILE}).")
    except Exception as e:
        print(f"Error while {step}: {e}")


if __name__ == "__main__":
    main()