# Jumping on the Clouds
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
# Time complexity: O(n)

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

i = 0
steps = 0
while (i < (n - 1)):
    if i + 2 <= n - 1:
        if c[i + 2] == 0:
            i += 1
    i += 1
    steps += 1
print (steps)