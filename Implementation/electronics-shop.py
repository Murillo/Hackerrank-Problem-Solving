# Electronics Shop
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/electronics-shop/problem
# Big O = O(n²)

def getMoneySpent(keyboards, drives, s):
    total_money = -1
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            sum_brands = keyboards[i] + drives[j]
            if sum_brands <= s and sum_brands > total_money:
                total_money = sum_brands

    return total_money

s,n,m = list(map(int, input().strip().split(' ')))
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))

print(getMoneySpent(keyboards, drives, s))