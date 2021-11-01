# Problem: Print in Reverse
# Url: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem
# Level: Easy
# Developer: Murillo Grübler

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')
        node = node.next
        if node:
            print(sep, end='')

######################################
#### Function to Print in Reverse ####
def reversePrint(head):
    def reverseRecursion(node):
        if node.next is not None:
            reverseRecursion(node.next)
        print(node.data)
    
    if head is not None:
        reverseRecursion(head)
######################################
        

if __name__ == '__main__':
    tests = int(input())
    for tests_itr in range(tests):
        llist_count = int(input())
        llist = SinglyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)
        reversePrint(llist.head)