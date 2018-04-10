# Library Fine
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/library-fine/problem
# Time complexity: O(1)

# Load library date
from datetime import datetime

def libraryFine(d1, m1, y1, d2, m2, y2):
    finish = datetime.strptime('{} {} {}'.format(m2, d2, y2), '%m %d %Y')
    retured = datetime.strptime('{} {} {}'.format(m1, d1, y1), '%m %d %Y')
    if retured < finish:
        return 0
    else:
        if m1 != m2 and y1 == y2:
            return (retured.month - finish.month) * 500
        elif y1 != y2:
            return (retured.year - finish.year) * 10000
        else:
            return (retured-finish).days * 15

d1, m1, y1 = list(map(int, input().strip().split(' ')))
d2, m2, y2 = list(map(int, input().strip().split(' ')))
print(libraryFine(d1, m1, y1, d2, m2, y2))