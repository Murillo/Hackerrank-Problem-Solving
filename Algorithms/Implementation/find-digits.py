# Find Digits
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/find-digits/problem
# Time Complexity = O(n²)

t = int(input().strip())
for a0 in range(t):
    count = 0
    n = input().strip()
    for i in range(len(n)):
        total_number = int(n)
        digit_number = int(n[i])
        if digit_number != 0 and total_number % digit_number == 0:
            count += 1
    print (count)
