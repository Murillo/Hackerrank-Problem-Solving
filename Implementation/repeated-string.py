# Repeated String
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/repeated-string/problem
# Time Complexity = O(n)

def repeated_string(text, total):
    if len(text) == 1 and text == 'a':
        return total

    new_text = ""
    for i in range(total):
        if len(new_text) < total:
            new_text += text
        else:
            new_text = new_text[:total]
    return len([new_text[i] for i in range(len(new_text)) if new_text[i] == 'a'])

s = input().strip()
n = int(input().strip())
print (repeated_string(s, n))