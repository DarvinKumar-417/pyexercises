"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:  A list of at least eight student grades.
# 2. Process: The program stores the grades, displays one grade,sorts the grades, and calculates the average.
# 3. Out: The complete list, one selected grade, the sorted list, and the average grade.
# 4. What my list is about, and what I computed from it:  I chose student grades because they can be used to calculate and analyze academic performance.


# Your code below
grades = [15, 12, 18, 14, 10, 16, 13, 17]

print("Whole list:", grades)

print("One item:", grades[2])

print("Sorted list:", sorted(grades))

average = sum(grades) / len(grades)
print("Average:", average)