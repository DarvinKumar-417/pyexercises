"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:Numbers entered by the user.
# 2. Process: The program keeps asking for numbers until the user enters 0. It counts the numbers and adds them together.
# 3. Out: The total number of numbers entered and their sum.
# 4. My stop condition, my attempt limit, my summary: The loop stops when the user enters 0.


# Your code below
total = 0
count = 0

number = int(input("Enter a number (0 to stop): "))

while number != 0:
    total = total + number
    count = count + 1

    number = int(input("Enter a number (0 to stop): "))

print("You entered", count, "numbers.")
print("The total is:", total)