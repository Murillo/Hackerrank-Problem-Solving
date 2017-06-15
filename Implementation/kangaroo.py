# There are two kangaroos on a number line ready to jump in the 
# positive direction (i.e, toward positive infinity). The first 
# kangaroo starts at location x1 and moves at a rate of v1 meters 
# per jump. The second kangaroo starts at location x2 and moves 
# at a rate of v2 meters per jump. Given the starting locations 
# and movement rates for each kangaroo, can you determine if 
# they'll ever land at the same location at the same time?]

# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/kangaroo

def kangaroo(x1, v1, x2, v2):
    if x1 <= x2 and v1 < v2:
        return "NO"
    elif x2 <= x1 and v2 < v1:
        return "NO"
    elif x1 == x2 and v1 == v2:
        return "YES"
    elif (v1 != v2) and ((x2-x1) % (v1-v2)) == 0:
        return "YES"
    else:
        return "NO"

x1, v1, x2, v2 = [int(points) for points in input().strip().split(' ')]
result = kangaroo(x1, v1, x2, v2)
print(result)

