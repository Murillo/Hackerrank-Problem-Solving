# Halloween Sale
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/halloween-sale/problem
# Time Complexity = O(n)

import os

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    price = result = last_price = 0
    while price <= s:
        if result == 0:
            last_price = p
        elif last_price - d > m:
            last_price = last_price - d
        else:
            last_price = m
        price += last_price
        result += 1
    return result - 1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    p, d, m, s = list(map(int, input().strip().split(' ')))
    answer = howManyGames(p, d, m, s)
    print (str(answer) + '\n')
    # fptr.write(str(answer) + '\n')
    # fptr.close()