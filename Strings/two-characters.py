# Two Characters
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/two-characters/problem

def validate(text):
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            return False
    return True

s_len = int(input().strip())
s = input().strip()
if s_len > 1:
    sl = list(s)
    max_len = 0
    for x in range(len(sl)):
        for y in range(x+1, len(sl)):
            if sl[x] != sl[y]:
                text = [c for c in s if c == sl[x] or c == sl[y]]
                if validate(text):
                    max_len = max(max_len, len(text))
    print (max_len)
else:
    print (0)