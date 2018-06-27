# Day of the Programmer
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/day-of-the-programmer/problem
# Time complexity: O(1)

import os

# Complete the solve function below.
def solve(year):
    if year == 1918:
        return "26.09.1918"
    elif (year <= 1917 and year % 4 == 0) or (year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
        return "12.09.{}".format(year)
    else:
        return "13.09.{}".format(year)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    year = int(input())
    result = solve(year)
    print (result + '\n')
    # fptr.write(result + '\n')
    # fptr.close()