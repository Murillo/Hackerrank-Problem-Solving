# HackerRank in a String!
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

q = int(input().strip())
for a0 in range(q):
    word = ['h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k']
    s = input().strip()
    for i in range(len(s)):
        if len(word) == 0:
            break
        if s[i] == word[0]:
            word.remove(s[i])
    print ("NO" if len(word) > 0 else "YES")