# Merge two sorted linked lists
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem
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

################################################################################
################################################################################
# Time Complexity: O(n)
# Space Complexity: O(n * 2)
# It will fail in some tests due to extra space due to recursion. 
def mergeLists2(head1, head2):
    def mergeListsRecursice(h1,h2,hr = None):
        if h1 is None and h2 is None:
            return hr
        
        if h1 is None:
            hr = SinglyLinkedListNode(h2.data)
            h2 = h2.next
            hr.next = mergeListsRecursice(h1, h2, hr.next)
        elif h2 is None:
            hr = SinglyLinkedListNode(h1.data)
            h1 = h1.next
            hr.next = mergeListsRecursice(h1, h2, hr.next)
        elif h1.data <= h2.data:
            hr = SinglyLinkedListNode(h1.data)
            h1 = h1.next
            hr.next = mergeListsRecursice(h1, h2, hr.next)
        else:
            hr = SinglyLinkedListNode(h2.data)
            h2 = h2.next
            hr.next = mergeListsRecursice(h1, h2, hr.next)
        return hr
    return mergeListsRecursice(head1, head2)

################################################################################
# Time Complexity: O(n)
# Space Complexity: O(n)
def mergeLists(head1, head2):
    hr = SinglyLinkedList()
    while head1 or head2:
        if head1 is None:
            hr.insert_node(head2.data)
            head2 = head2.next
        elif head2 is None:
            hr.insert_node(head1.data)
            head1 = head1.next
        elif head1.data <= head2.data:
            hr.insert_node(head1.data)
            head1 = head1.next
        else:
            hr.insert_node(head2.data)
            head2 = head2.next
    return hr.head
################################################################################
################################################################################

if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)
        print_singly_linked_list(llist3, ' ')