# Priyanka and Toys
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/priyanka-and-toys/problem
# Time complexity: O(n log n)

def toys(w):
    w.sort()
    total = 1
    free_toys = w[0] + 4
    for i in range(1, len(w)):
        if w[i] > free_toys:
            total += 1
            free_toys = w[i] + 4
    return total

n = int(input().strip())
w = list(map(int, input().strip().split(' ')))
print(toys(w))