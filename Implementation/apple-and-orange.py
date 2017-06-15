# Sam's house has an apple tree and an orange tree that yield an 
# abundance of fruit. In the diagram below, the red region denotes 
# his house, where s is the start point and t is the end point. 
# The apple tree is to the left of his house, and the orange tree 
# is to its right. You can assume the trees are located on a single 
# point, where the apple tree is at point a and the orange tree 
# is at point b.

# When a fruit falls from its tree, it lands d units of distance 
# from its tree of origin along the x-axis. A negative value of d 
# means the fruit fell d units to the tree's left, and a positive 
# value of d means it falls d units to the tree's right.

# Given the value of d for m apples and n oranges, can you determine 
# how many apples and oranges will fall on Sam's house (i.e., in the 
# inclusive range [s,t])? Print the number of apples that fall on 
# Sam's house as your first line of output, then print the number of 
# oranges that fall on Sam's house as your second line of output.

# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/apple-and-orange

s,t = [int(points) for points in input().strip().split(' ')]
a,b = [int(points) for points in input().strip().split(' ')]
m,n = [int(points) for points in input().strip().split(' ')]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

apples_home = []
oranges_home = []
for i in range(m):
    pos_apple = a + apple[i]
    if pos_apple >= s and pos_apple <= t:
        apples_home.append(apple[i])

for i in range(n):
    pos_orange = b + orange[i]
    if pos_orange >= s and pos_orange <= t:
        oranges_home.append(orange[i])
    
print (len(apples_home))
print (len(oranges_home))