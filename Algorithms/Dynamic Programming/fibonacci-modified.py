# Fibonacci Modified
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/fibonacci-modified/problem

def fibonacci(t0, t1, n):
    i = 2
    r = 0
    while (i < n):
        r = t0 + (t1 ** 2)
        t0 = t1
        t1 = r
        i += 1
    return r

t0, t1, n = input().strip().split(' ')
t0, t1, n = [int(t0), int(t1), int(n)]

print (fibonacci(t0, t1, n))