# Strong Password
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/strong-password/problem
# Time complexity: O(n)

def minimumNumber(n, password):
    total = 0
    at_least = 6
    numbers = list([i for i in "0123456789"]) 
    lower_case = list([i for i in "abcdefghijklmnopqrstuvwxyz"])
    upper_case = list([i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])
    special_characters = list([i for i in "!@#$%^&*()-+"])

    if not any(x in numbers for x in password):
        total += 1
    if not any(x in lower_case for x in password):
        total += 1
    if not any(x in upper_case for x in password):
        total += 1
    if not any(x in special_characters for x in password):
        total += 1

    rest = at_least - len(password)
    total = rest if rest > 0 and rest >= total else total
    return total

n = int(input().strip())
password = input().strip()
print(minimumNumber(n, password))