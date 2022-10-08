# Problem: Left Rotation
# Url: https://www.hackerrank.com/challenges/array-left-rotation/problem
# Level: Easy
# Developer: Murillo Grübler

###################################
def rotateLeft(d, arr):
    def rearrange(left_pointer, right_pointer):
        while left_pointer < right_pointer:
            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
            left_pointer += 1
            right_pointer -= 1

    total_arr = len(arr)
    total_rotate = d % total_arr
    
    rearrange(0, total_arr - 1)
    rearrange(total_arr - total_rotate, total_arr - 1)
    rearrange(0, total_arr - total_rotate - 1)

    return arr
###################################

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = rotateLeft(d, arr)
    print(' '.join(map(str, result)))