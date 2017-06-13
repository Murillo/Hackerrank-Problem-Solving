# Consider a staircase of size n = 4:
#    #
#   ##
#  ###
# ####
# Observe that its base and height are both equal to 4, 
# and the image is drawn using # symbols and spaces. The 
# last line is not preceded by any spaces.
# Write a program that prints a staircase of size n.

# Developer: Murillo Grubler

n = int(input().strip())

for i in range(n):
    line = ""
    for j in range(n):
        if j < ((n - 1) - i):
            line = line + " "
        else:
            line = line + "#"
    print (line)