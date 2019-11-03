# Tree: Level Order Traversal
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
# Time complexity: O(n)

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

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    seq = [root]
    while (len(seq) > 0):
        node = seq[0]
        seq.pop(0)
        print(node.info, end=" ")
        if node.left is not None:
            seq.append(node.left)
        if node.right is not None:
            seq.append(node.right)

        

if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())
    arr = list(map(int, input().split()))
    for i in range(t):
        tree.create(arr[i])
    levelOrder(tree.root)