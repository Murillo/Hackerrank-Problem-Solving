# Problem: Reverse a doubly linked list
# Url: https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem
# Level: Easy
# Developer: Murillo Grübler

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node):
    while node:
        print (str(node.data))
        node = node.next

##################################################
#### Function to Reverse a doubly linked list ####
def reverse(head):
    def reverseRecursion(node):
        node.next, node.prev = node.prev, node.next
        if node.prev is None:
            return node
        return reverseRecursion(node.prev)

    if head is not None:
        return reverseRecursion(head)
    return None
##################################################
        

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        llist_count = int(input())
        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)
        print_doubly_linked_list(llist1)
