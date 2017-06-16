# Consider two sets of positive integers, A = {a0, a1, ..., an-1} 
# and B = {b0, b1, ... , bm-1}. We say that a positive integer, x, 
# is between sets A and B if the following conditions are satisfied:

# 1. All elements in A are factors of x.
# 2. x is a factor of all elements in B.

# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/between-two-sets
# Reference: http://www.4dsolutions.net/cgi-bin/py2html.cgi?script=/ocn/python/primes.py

# Define functions
def gcd(a,b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b / gcd(a, b)

def GCD(terms):
    "Return gcd of a list of numbers."
    result = terms[0]
    for i in range(1, len(terms)):
        result = gcd(result, terms[i])
    return result

def LCM(terms):
    "Return lcm of a list of numbers."
    result = 1
    for t in terms:
        result = lcm(result, t)
    return result

def getTotalX(a, b):
    lcm_value = LCM(a)
    gcd_value = GCD(b)
    counter = 0
    multiple_lcm = lcm_value
    while multiple_lcm <= gcd_value:
        if (gcd_value % multiple_lcm) == 0:
            counter += 1
        multiple_lcm += lcm_value
    return counter

n, m = [int(points) for points in input().strip().split(' ')]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)