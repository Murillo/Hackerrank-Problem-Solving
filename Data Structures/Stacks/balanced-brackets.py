# Balanced Brackets
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/balanced-brackets/problem
# Time complexity: O(n)

def isBalanced(s):
    cl = ["}","]",")"]
    op = ["{","[","("]
    seq = []
    for i in range(len(s)):
        if len(seq) == 0 and s[i] in cl:
            seq.append(s[i])
            break 

        if s[i] in op:
            seq.append(s[i])
        elif len(seq) > 0 and op.index(seq[len(seq)-1]) == cl.index(s[i]):
            seq.pop()
        else:
            break

    if len(seq) == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        print(result + '\n')