# Counting Valleys
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/counting-valleys/problem
# big-O notation = O(n)

def counting_valleys(n, ar):
    level = 0
    sea_level = False
    count_down_level = 0
    for i in range(n):
        level = level + 1 if ar[i] == "U" else level - 1
        if not sea_level and level < 0:
            sea_level = True
            count_down_level += 1
        elif sea_level and level >= 0:
            sea_level = False
    return count_down_level

n = int(input().strip())
ar = input().strip()
print (counting_valleys(n, ar))