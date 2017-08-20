# Even Tree
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/even-tree/problem

class Node(object):

    def __init__(self, value=None):
        self._value = value
        self._parent = None
        self._descendant = 0

    def set_parent(self, parent_val):
        self._parent = parent_val
        ancestor = parent_val
        while (ancestor != None):
            ancestor._descendant += 1
            ancestor = ancestor.parent

    def get_parent(self):
        return self._parent

    def set_descendant(self, descendant):
        self._descendant = descendant
       
    def get_descendant(self):
        return self._descendant

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    @staticmethod
    def find_parent(nodes, parent):
        for node in nodes:
            if node.value == parent:
                return node
        return None

    parent      = property(get_parent, set_parent)
    descendant  = property(get_descendant, set_descendant)
    value       = property(get_value, set_value)


edges_removeds = 0
nodes = []
n, m = input().strip().split(' ')
for i in range(int(m)):
    children, parent = [int(node) for node in input().strip().split(' ')]
    if i == 0:
        node_parent = Node(parent)
        nodes.append(node_parent)

        node_children = Node(children)
        node_children.parent = node_parent
        nodes.append(node_children)
    else:
        node_children = Node(children)
        node_children.parent = Node.find_parent(nodes, parent)
        nodes.append(node_children)

for node in nodes:
    if node.value > 1 and node.descendant > 0 and node.descendant % 2 == 1:
        edges_removeds += 1

print (edges_removeds)