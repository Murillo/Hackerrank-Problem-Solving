# Delete duplicate-value nodes from a sorted linked list
# Developer: Murillo Grübler
# https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem
# Time complexity: O(n)

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

def print_singly_linked_list(list, char_separator):
    while list is not None:
        print(list.data,end=char_separator)
        list = list.next

#################################################################
#################################################################
### Time complexity: O(n)
### Space complexity: O(n)
def removeDuplicates(llist):
    head = llist
    while llist is not None:
        if llist.next and llist.data == llist.next.data:
            llist.next = llist.next.next
        else:
            llist = llist.next
    return head
#################################################################
#################################################################


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        llist_count = int(input())
        llist = SinglyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)
        llist1 = removeDuplicates(llist.head)
        print_singly_linked_list(llist1, ' ')