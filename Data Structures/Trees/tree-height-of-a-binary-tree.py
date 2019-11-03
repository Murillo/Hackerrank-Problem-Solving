# Tree: Height of a Binary Tree
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
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

'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 

       // this is a node of the tree , which contains info as data, left , right
'''
def calculate_height(root, current_level, height):
    height = height + 1 if current_level > height else height
    if root.left is not None:
        height = calculate_height(root.left, current_level + 1, height)
    if root.right is not None:
        height = calculate_height(root.right, current_level + 1, height)
    return height


def height(root):
    if root is None:
        return 0
    return calculate_height(root, 0, 0)


tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))
for i in range(t):
    tree.create(arr[i])
print(height(tree.root))
