# Problem: Cycle Detection
# Url: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
# Level: Medium
# Developer: Murillo Grübler
# Technique: floyd cycle detection algorithm

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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

###################################
#### Function to detect cycle. ####
def has_cycle(head):
    if not head or not head.next:
        return False
    slower = head
    faster = head.next
    while (faster and faster.next):
        if slower == faster:
            return True
        slower = slower.next
        faster = faster.next.next
    return False
###################################

if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())
        llist_count = int(input())
        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1)
        temp = llist.head

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count-1:
                temp = temp.next

        temp.next = extra
        result = has_cycle(llist.head)
        print(str(int(result)))
