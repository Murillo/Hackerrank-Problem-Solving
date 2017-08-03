# Super Reduced String
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/reduced-string

def remove_pair_item(ar):
    remove_any_char = False
    last_string = ""
    for i in range((len(ar) - 1), 0, -1):
        if last_string == ar[i]:
            ar.pop(i + 1)
            ar.pop(i)
            remove_any_char = True
            #last_string = ""
            break
        else:
            last_string = ar[i]
    return remove_any_char, ar

def super_reduced_string(ar):
    if len(ar) > 0:
        count = 0
        chars = ar
        removed_char = True
        while (removed_char):
            removed_char, chars = remove_pair_item(chars)
            if removed_char:
                count += 1
        if count > 0:
            return chars
    return "Empty String"
    
s = list(input().strip())
print(super_reduced_string(s))
#print ("".join(str(x) for x in s))