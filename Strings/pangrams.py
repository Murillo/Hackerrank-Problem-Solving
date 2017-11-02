# Pangrams
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/pangrams/problem

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
count = len(alphabet)
st = input()
letters = 0
letters_used = []
for i in range(len(st)):
    if st[i].upper() in alphabet and st[i].upper() not in letters_used:
        letters_used.append(st[i].upper())
        letters += 1
print ("pangram" if letters == count else "not pangram")