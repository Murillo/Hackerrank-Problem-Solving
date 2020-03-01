# Delete a Node
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
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
def deleteNode(head, position):
    if position > 0:
        temp = head
        for i in range(position - 1):
            temp = temp.next
        temp.next = temp.next.next
    else:
        head = head.next
    return head
###############################################

if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()
    
    ar = [9, 15, 4, 7, 19, 2, 6, 20]
    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())
    llist1 = deleteNode(llist.head, position)
    print_singly_linked_list(llist1)