# Tree: Top View
# Developer: Murillo Grübler
# https://www.hackerrank.com/challenges/tree-top-view/problem

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

###################################################
### Time complexity: O(n)
### Space complexity: O(n)
###################################################
def topView(root):
    min_level = 0
    max_level = 0
    nodes_viwed = {}
    stack_nodes = [[root, 0]]

    while len(stack_nodes) > 0:
        val = stack_nodes.pop(0)
        node = val[0]
        level = val[1]
        if level not in nodes_viwed:
            nodes_viwed[level] = node.info
            min_level = min(min_level, level)
            max_level = max(max_level, level)
        
        if node.left:
            stack_nodes.append([node.left, level - 1])

        if node.right:
            stack_nodes.append([node.right, level + 1])


    for i in range(min_level, max_level + 1):
        print (nodes_viwed[i], end = " ")
###################################################


tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)