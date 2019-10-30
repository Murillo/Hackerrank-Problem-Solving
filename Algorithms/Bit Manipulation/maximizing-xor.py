# Maximizing XOR
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/maximizing-xor/problem
# Time complexity: O(n²)

def maximizingXor(l, r):
    result = []
    for i in range(l, r + 1):
        for j in range(l, r + 1):
            result.append(i ^ j)
    return max(result)

l = int(input().strip())
r = int(input().strip())
print(maximizingXor(l, r))