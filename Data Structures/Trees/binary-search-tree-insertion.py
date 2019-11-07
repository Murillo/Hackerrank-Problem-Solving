# Binary Search Tree : Insertion
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
# Time complexity: O(log N)

class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

    #Node is defined as
    #self.left (the left child of the node)
    #self.right (the right child of the node)
    #self.info (the value of the node)
    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if current.info > val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif current.info < val: 
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))
for i in range(t):
    tree.insert(arr[i])
preOrder(tree.root)