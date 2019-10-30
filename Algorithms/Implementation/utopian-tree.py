# Utopian Tree
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/utopian-tree/problem
# Time Complexity = O(n)

def cycle(period):
    height = 1
    for i in range(period):
        if i % 2 == 0:
            height = height * 2
        else:
            height = height + 1
    return height;

t = int(input().strip())
for a0 in range(t):
    print(cycle(int(input().strip())))