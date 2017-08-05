# Two Characters
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/two-characters/problem

# descobrir todos os chars diferentes
# obter todas as combinacoes possiveis somando a quantidade de chars e diminuindo por 2
# remover os chars da string, sobrando apenas duas strins e elas nao podem estar em sequencia
# somar o char que possui mais caracteres

def single_character(ar):
    chars = []
    for i in range(len(ar)):
        if ar[i] not in chars:
            chars.append(ar[i])
    return chars

def get_combinations(ar_chars):
    combinations = []
    chars_possible = (len(ar_chars) - 2) * (len(ar_chars) - 2)
    
    
    return []

def remove_chars():

    return []

s_len = int(input().strip())
s = list(input().strip())
print (single_character(s))
last_char = ""
max_len = 0
