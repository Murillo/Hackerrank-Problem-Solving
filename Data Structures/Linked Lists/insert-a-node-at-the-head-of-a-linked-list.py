# Insert a node at the head of a linked list
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
# Time complexity: O(1)

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(head):
    while head:
        print (head.data)
        head = head.next

def insertNodeAtHead(llist, data):
    if llist is None:
        return SinglyLinkedListNode(data)
    else:
        next_temp = llist
        llist = SinglyLinkedListNode(data)
        llist.next = next_temp
    return llist

if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()
    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    print_singly_linked_list(llist.head)