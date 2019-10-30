# Diagonal Difference
# Developer: Murillo Grubler

n = int(input().strip())
a = []
value_left = 0
value_right = 0
left_index = 0
right_index = n - 1
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    value_left  = value_left + a_t[left_index]
    value_right = value_right + a_t[right_index]
    left_index  += 1
    right_index -= 1

print (abs(value_left - value_right))