# Conversation with the AI

Written automatically by `tutor.py`. Add your own notes under any entry: what you tried, what broke, what you changed. Those notes are what is graded.

---
## 2026-10-09 13:20, in .

**Me:** @what is lists@

**Tutor:**

Refused, off topic.

---
## 2026-10-09 13:20, in .

**Me:** @what is lists

**Tutor:**

A list is a built-in Python container that stores an ordered, changeable collection of items.

```python
# Example list
fruits = ["apple", "banana", "cherry"]

# Access the second item
second_fruit = fruits[1]  # TODO: what index gives the first item?

# Change the third item
fruits[2] = "orange"  # TODO: which index is updated here?
```

Question: In the list `fruits`, what is the index of the first element?

---
## 2026-11-03 11:09, in .

**Me:** “How can I read a CSV file in Python?”

**Tutor:**

Reading a CSV file in Python is done with the csv module.

```python
import csv

# TODO: replace 'data.csv' with your file path
with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)   # TODO: choose delimiter if not comma
    for row in reader:
        print(row)                 # TODO: adapt to your data
```

What argument tells csv.reader how to split each line?

---
## 2026-11-03 11:09, in .

**Me:** “How do I calculate CTR using clicks and impressions?”

**Tutor:**

Calculating CTR (Click-Through Rate) from clicks and impressions.

CTR is clicks divided by impressions, then multiplied by 100 to get a percentage.

```python
def calculate_ctr(clicks: int, impressions: int) -> float:
    # TODO: compute CTR here
    return 0.0
```

What function takes two numbers and returns their quotient?

---
## 2026-11-03 11:10, in .

**Me:** “How can I calculate ROAS from revenue and cost?”

**Tutor:**

Calculating ROAS (Return on Advertising Spend) from revenue and cost.

ROAS is simply revenue divided by cost.

```python
def calculate_roas(revenue: float, cost: float) -> float:
    # TODO: divide revenue by cost and return the result
    pass
```

What function do you use to perform the division?

---
## 2026-11-03 11:10, in .

**Me:** “How can I ignore rows where impressions are empty?”

**Tutor:**

Concept: filtering rows with missing values in a specific column.

```python
import csv

def ignore_empty_impressions(rows):
    # rows is a list of dicts from csv.DictReader
    # TODO: return only rows where the 'impressions' column is not empty
    return [row for row in rows if ...]
```

Question: Which string method removes whitespace and checks that a value is not empty?

---
## 2026-11-03 11:10, in .

**Me:** “How do I find the campaign with the highest CTR?”

**Tutor:**

Finding the campaign with the highest CTR is about **filtering and finding the maximum**.

```python
import csv

def highest_ctr(campaigns):
    # campaigns is a list of dicts, each dict has a 'campaign' and 'ctr' key
    # TODO: keep only the campaign with the highest ctr
    # TODO: return its name
    pass

# Toy data
rows = [
    {'campaign': 'spring', 'ctr': 0.02},
    {'campaign': 'summer', 'ctr': 0.05},
    {'campaign': 'autumn', 'ctr': 0.03}
]

print(highest_ctr(rows))  # should print 'summer'
```

What function gives you the row with the largest ctr?

---
## 2026-11-03 11:12, in .

**Me:** “How do I save the players name, score and date into result.csv?”

python tutor.py “How do I save the players name, score and date into result.csv?”

**Tutor:**

Refused, off topic.

---
## 2026-11-03 11:12, in .

**Me:** “How can I use try and except so my program does not crash?

**Tutor:**

Using try and except to handle errors.

```python
def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        result = None
    return result

# TODO: call safe_divide with 10 and 2, then with 10 and 0
```

What exception does the except block catch in this function?
