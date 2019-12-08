# Reverse a linked list
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
# Time complexity of reverse function: O(n)

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

# Complete the reverse function below.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
def reverse(head):
    ln = SinglyLinkedListNode(head.data)
    temp_node = head.next
    while temp_node:
        next_ln = ln
        ln = SinglyLinkedListNode(temp_node.data)
        ln.next = next_ln
        temp_node = temp_node.next
    return ln

if __name__ == '__main__':
    tests = int(input())
    for tests_itr in range(tests):
        llist_count = int(input())
        llist = SinglyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        result = reverse(llist.head)
        while result:
            print (result.data, end=' ')
            result = result.next
