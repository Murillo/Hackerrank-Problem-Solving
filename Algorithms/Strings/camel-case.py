# CamelCase
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/camelcase/problem
# Time complexity: O(n)

letters = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
string = input().strip()
total = 1
for i in range(len(string)):
    if string[i] in letters:
        total += 1
print (total)
