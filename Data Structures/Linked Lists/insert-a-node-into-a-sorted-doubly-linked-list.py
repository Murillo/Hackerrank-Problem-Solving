# Problem: Inserting a Node Into a Sorted Doubly Linked List
# Url: https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem
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

#######################################################################
#### Function to Inserting a Node Into a Sorted Doubly Linked List ####
def sortedInsert(head, data):
    def sortedRecursion(node):
        if not node:
            return DoublyLinkedListNode(data)
        
        if data < node.data:
            new_node = DoublyLinkedListNode(data)
            new_node.next = node
            node.prev = new_node
            return new_node

        next_node = sortedRecursion(node.next)
        node.next = next_node
        next_node.prev = node
        return node

    if head:
        return sortedRecursion(head)
        
    return DoublyLinkedListNode(data)

#######################################################################

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())
        llist1 = sortedInsert(llist.head, data)
        print_doubly_linked_list(llist1)