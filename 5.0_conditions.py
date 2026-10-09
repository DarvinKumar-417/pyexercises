# 5.0_conditions
# 1. In:
# The program asks the user to enter the number of hours
# they study per week.

# 2. Process:
# The program compares the entered number with four ranges
# and uses if, elif, and else to choose the correct message.

# 3. Out:
# A message describing the student's weekly study habits.

# 4. My ranges, my boundaries, my messages:
# Range 1: 0 to 9 hours — "You should try to study more."
# Range 2: 10 to 19 hours — "You have a good start."
# Range 3: 20 to 29 hours — "You have a strong study routine."
# Range 4: 30 hours or more — "You dedicate a lot of time to studying."
#
# I chose these ranges because they represent increasing amounts
# of weekly study time. The cut-offs make it easy to compare habits.
# Each range includes its lower boundary. For example, 10 belongs
# to Range 2, not Range 1.

# Your code below

hours = int(input("How many hours do you study per week? "))

if hours < 0:
    print("Please enter a non-negative number.")
elif hours < 10:
    print("You should try to study more.")
elif hours < 20:
    print("You have a good start.")
elif hours < 30:
    print("You have a strong study routine.")
else:
    print("You dedicate a lot of time to studying.")


