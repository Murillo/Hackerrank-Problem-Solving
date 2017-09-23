# Extra Long Factorials
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/extra-long-factorials/problem
# Time Complexity = O(n)

def factorial(n):
    if n == 1:
        return 1

    total = n
    while (n > 0):
        if n == total:
            total = total * (n - 1)
            n -= 2
        else:
            total = total * n
            n -= 1
    return total

n = int(input().strip())
print (factorial(n))