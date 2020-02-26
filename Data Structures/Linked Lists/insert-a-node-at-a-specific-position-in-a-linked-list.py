# Insert a node at a specific position in a linked list
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
# Time complexity: O(n)

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
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

def print_singly_linked_list(head):
    while head:
        print (head.data)
        head = head.next

###############################################
def insertNodeAtPosition(head, data, position):
    temp = head
    if position > 0:
        for i in range(position - 1):
            temp = temp.next
        temp_next = temp.next
        temp.next = SinglyLinkedListNode(data)
        temp.next.next = temp_next
    else:
        head = SinglyLinkedListNode(data)
        head.next = temp
    return head
###############################################

if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()
    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())
    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)
    print_singly_linked_list(llist_head)