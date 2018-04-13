# Lonely Integer
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/lonely-integer/problem
# Time complexity: O(n²)

def lonelyinteger(a):
    lonely = []
    for i in range(len(a)):
        if a.count(a[i]) % 2 != 0:
            lonely.append(a[i])
    return " ".join(map(str, lonely))

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
print(lonelyinteger(a))