# Mars Exploration
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/mars-exploration/problem

m = input().strip()
total_s = len(m) / 3
count = 0
chars_changed = 0

for i in range(1, int(total_s) + 1):
    if m[count] != "S":
        chars_changed += 1

    if m[count + 1] != "O":
        chars_changed += 1

    if m[count + 2] != "S":
        chars_changed += 1
    count += 3

print (chars_changed)