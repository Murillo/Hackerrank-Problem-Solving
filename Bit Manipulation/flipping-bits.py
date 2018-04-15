# Flipping bits
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/flipping-bits/problem
# Reference: https://en.wikipedia.org/wiki/4,294,967,295

# Time complexity: O(1)
def flippingBits(N):
    return N^4294967295

# Start algorithm
n = int(input().strip())
for a0 in range(n):
    print(flippingBits(int(input().strip())))