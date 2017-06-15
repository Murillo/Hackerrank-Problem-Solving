# HackerLand University has the following grading policy:
# Every student receives a  in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.

# Sam is a professor at the university and likes to round each 
# student's  grade according to these rules:

# If the difference between the grade and the next multiple of 5 
# is less than 3, round grade up to the next multiple of 5.

# If the value of grade is less than 38, no rounding occurs as the 
# result will still be a failing grade.

# For example, grade = 84 will be rounded to 85 but grade = 29 
# will not be rounded because the rounding would result in a number 
# that is less than 40.

# Developer: Murillo Grubler
# Link https://www.hackerrank.com/challenges/grading

def next_multiple(number):
    max_multiple = True
    start = 1
    while (max_multiple):
        if (start * 5) > number:
            max_multiple = False
        else:
            start += 1
    return start

# Function that rounds the students' grades
def solve(grades):
    new_grades = []
    for i in range(len(grades)):
        if grades[i] >= 38: 
            new_value = (next_multiple(grades[i]) * 5) - grades[i]
            if new_value < 3:
                new_grades.append(grades[i] + new_value)
                continue
        new_grades.append(grades[i])
    return new_grades

# Get data
n = int(input().strip())
grades = []
for grades_i in range(n):
   grades.append(int(input().strip()))

# Resolve the problem and show on the screen
result = solve(grades)
print ("\n".join(map(str, result)))