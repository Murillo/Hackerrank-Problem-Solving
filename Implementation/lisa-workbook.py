# Lisa's Workbook
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/lisa-workbook/problem
# Time complexity: O(n³)

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
                pg_remaining = read + p
            else:
                pg_remaining = read + total       
            for k in range(read, pg_remaining):
                if pages == k:
                    special += 1
                read += 1
            pages += 1
    return special

n,k = list(map(int, input().strip().split(' ')))
chapters = list(map(int, input().strip().split(' ')))
print (workbook(n, k, chapters))