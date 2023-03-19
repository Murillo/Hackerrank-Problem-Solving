# Equal Stacks
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/equal-stacks/problem
# Time complexity: O(n)
# Space complexity: O(1)

############################################################
def equalStacks(h1, h2, h3):
    sum_h1 = sum(h1)
    sum_h2 = sum(h2)
    sum_h3 = sum(h3)
    turn = 1
    result = 0

    # If all stacks comes with same height
    if sum_h1 == sum_h2 and sum_h2 == sum_h3:
        return sum_h1

    while not (sum_h1 == sum_h2 and sum_h2 == sum_h3):
        # Checking if h1 and h2 share same height
        while sum_h1 != sum_h2:
            if turn == 1:
                h1_val = h1.pop(0)
                sum_h1 -= h1_val
            else:
                h2_val = h2.pop(0)
                sum_h2 -= h2_val
            turn = 1 if sum_h1 > sum_h2 else 2

        # If h1 or h2 are 0 it means the 3 stacks don't share same height
        if sum_h1 == 0 or sum_h2 == 0:
            break

        # Checking if h3 has same height as the h1.
        # At this point h1 and h2 have same height
        while sum_h1 < sum_h3:
            h3_val = h3.pop(0)
            sum_h3 -= h3_val
            if sum_h3 == sum_h1:
                break
        
        # If h3 is smaller than h1 it removes the first value from h1 
        # to initialize the first check between h1 and h2
        if sum_h1 != sum_h3:
            h1_val = h1.pop(0)
            sum_h1 -= h1_val
            turn = 2

        # If all stacks has same height it set the final result
        if sum_h1 == sum_h2 and sum_h2 == sum_h3:
            result = sum_h3

    return result
############################################################
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n1 = int(first_multiple_input[0])
    n2 = int(first_multiple_input[1])
    n3 = int(first_multiple_input[2])
    h1 = list(map(int, input().rstrip().split()))
    h2 = list(map(int, input().rstrip().split()))
    h3 = list(map(int, input().rstrip().split()))
    result = equalStacks(h1, h2, h3)
    print (result)