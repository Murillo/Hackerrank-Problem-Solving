# Lisa's Workbook
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/lisa-workbook/problem

import math

def workbook(n, p, chapters):
    special = 0
    pages = 0
    for i in range(n):
        pages_chapt = math.ceil(chapters[i] / p)
        total = chapters[i]
        read = 0
        for j in range(pages_chapt):
            if total > p:
                total = total - p
                if total < p:
                    pg_remaining = read + p
                else:
                    pg_remaining = read + total
            else:
                pg_remaining = read + total       
            for k in range(read, pg_remaining):
                if pages == k:
                    special += 1
                read += 1
            pages += 1
    return special

#n,k = list(map(int, input().strip().split(' ')))
#chapters = list(map(int, input().strip().split(' ')))
n, k = 25, 10
chapters = [1, 29, 94, 15, 87, 100, 20, 55, 100, 45, 82, 80, 100, 100, 3, 53, 100, 2, 100, 100, 100, 100, 100, 100, 1]

#n, k = 5, 3
#chapters = [4, 2, 6, 1, 10]
print (workbook(n, k, chapters))