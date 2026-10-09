"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of student grades from Exercise 4.0.
# 2. Process: The program goes through every grade and gets its position.It also checks whether the grade is above or below 10.
# 3. Out:For every grade, the program displays its position, the grade, and whether it is above or below 10.
# 4. What I compute for each item, and why it is worth showing: I am using the student grades list from Exercise 4.0. I use the grade and its position to analyze student performance.


# Your code below
grades = [15, 12, 18, 14, 10, 16, 13, 17]

for position, grade in enumerate(grades):
    if grade >= 10:
        result = "Pass"
    else:
        result = "Fail"

    print("Position:", position, "| Grade:", grade, "| Result:", result)