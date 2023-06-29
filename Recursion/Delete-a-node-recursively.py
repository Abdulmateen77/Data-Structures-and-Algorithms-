from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteNodeRec(head, pos):
    # Recursive function to delete a node at the given position in a linked list
    if head is None:
        return head

    # If the position is 0, delete the head node
    if pos == 0:
        head = head.next
        return head

    # Recursively delete the node at the next position
    deletednode = deleteNodeRec(head.next, pos - 1)
    head.next = deletednode
    return head

def takeInput():
    # Function to take input for the linked list
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
    # Function to print the linked list
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()

# Main program
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    pos = int(stdin.readline().rstrip())

    newHead = deleteNodeRec(head, pos)
    printLinkedList(newHead)

    t -= 1
