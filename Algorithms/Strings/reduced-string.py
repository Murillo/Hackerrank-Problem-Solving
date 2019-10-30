# Super Reduced String
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/reduced-string

def remove_pair_item(ar):
    last_string = ""
    total = len(ar) - 1
    for i in range(total, -1, -1):
        if last_string == ar[i]:
            ar.pop(i + 1)
            ar.pop(i)
            return True, ar
        else:
            last_string = ar[i]
    return False, ar

def super_reduced_string(ar):
    if len(ar) > 0:
        count = 0
        chars = ar
        removed_char = True
        while (removed_char):
            removed_char, chars = remove_pair_item(chars)
        if len(chars) > 0:
            return chars
    return "Empty String"
    
s = list(input().strip())
result = super_reduced_string(s)
print ("".join(str(x) for x in result))