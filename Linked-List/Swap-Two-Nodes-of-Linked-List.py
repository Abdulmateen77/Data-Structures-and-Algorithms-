from sys import stdin

# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def swapNodes(head, i, j):
    # Check if the head is None or there is only one node
    if head is None or head.next is None:
        return head

    # Check if the given indices are valid
    if i == j:
        return head

    # Initialize variables for the first node
    node1 = head
    prevNode1 = None
    count1 = 0

    # Initialize variables for the second node
    node2 = head
    prevNode2 = None
    count2 = 0

    # Traverse the linked list to find the nodes at indices i and j
    while node1 is not None and count1 != i:
        prevNode1 = node1
        node1 = node1.next
        count1 += 1

    while node2 is not None and count2 != j:
        prevNode2 = node2
        node2 = node2.next
        count2 += 1

    # If either node1 or node2 is None, indices are out of range
    if node1 is None or node2 is None:
        return head

    # Update the links to swap the nodes
    if prevNode1 is not None:
        prevNode1.next = node2
    else:
        head = node2

    if prevNode2 is not None:
        prevNode2.next = node1
    else:
        head = node1

    # Swap the next pointers of node1 and node2
    temp = node1.next
    node1.next = node2.next
    node2.next = temp

    return head


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while i < len(datas) and datas[i] != -1:
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# Main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1
