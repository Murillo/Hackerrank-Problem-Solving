# Repeated String
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/repeated-string/problem
# Time Complexity = O(n)

def repeated_string(text, total):
    if len(text) == 1 and text == 'a':
        return total

    add_value = 0
    if text.find('a')!=-1:
        add_value = len([text[i] for i in range(len(text)) if text[i] == 'a'])
    amount_str = 0
    new_text = ""
    for i in range(total):
        if len(new_text) < total:
            new_text += text
            if add_value > 0:
                amount_str += add_value
        else:
            diff = (len(new_text) - total) - 1
            text_out = new_text[(total - diff):total]
            amount_str -= len([text_out[i] for i in range(len(text_out)) if text_out[i] == 'a'])
            new_text = new_text[:total]
            break
    return amount_str

s = input().strip()
n = int(input().strip())
print (repeated_string(s, n))