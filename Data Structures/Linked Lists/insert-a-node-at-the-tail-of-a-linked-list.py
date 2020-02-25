# Insert a Node at the Tail of a Linked List
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

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

def insertNodeAtTail(head, data):
    if head is None:
        return SinglyLinkedListNode(data)
    elif head.next is None:
        head.next = SinglyLinkedListNode(data)
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = SinglyLinkedListNode(data)
    return head

def insertNodeAtTailRecursive(head, data):
    if head is None:
        return SinglyLinkedListNode(data)
    elif head.next is None:
        head.next = SinglyLinkedListNode(data)
    else:
        insertNodeAtTail(head.next, data)
    return head

if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()
    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head
    print_singly_linked_list(llist.head)