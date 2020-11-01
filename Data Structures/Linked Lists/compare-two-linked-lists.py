# Compare two linked lists
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/compare-two-linked-lists/problem
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

###############################################
def compare_lists(llist1, llist2):
    def compare_node(node1, node2):
        if node1 is None and node2 is None:
            return 1

        if (node1 is None and node2 is not None) or (node1 is not None and node2 is None):
            return 0

        if node1.data != node2.data:
            return 0

        result = compare_node(node1.next, node2.next)
        return 1 if result != 0 else 0

    return compare_node(llist1, llist2)
###############################################

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

        result = compare_lists(llist1.head, llist2.head)
        print(str(int(result)) + '\n')