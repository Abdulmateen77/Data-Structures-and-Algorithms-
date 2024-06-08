from sys import stdin

# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def skipMdeleteN(head, M, N):
    # If the linked list is empty or has only one node, return the head
    if head is None or head.next is None:
        return head

    # If M is 0, return None to indicate an empty linked list
    if M == 0:
        return None

    current = head
    prev = None

    while current is not None:
        # Skip M-1 nodes
        for i in range(M - 1):
            if current is None:
                return head
            prev = current
            current = current.next

        # Delete N nodes
        for i in range(N):
            if current is None:
                break
            current = current.next

        # Update the link of the previous node to the current node
        if prev is not None:
            prev.next = current

    return head


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
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
    # Traverse the linked list and print the data of each node
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# Main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    m_n = stdin.readline().strip().split(" ")

    m = int(m_n[0])
    n = int(m_n[1])

    newHead = skipMdeleteN(head, m, n)
    printLinkedList(newHead)

    t -= 1
