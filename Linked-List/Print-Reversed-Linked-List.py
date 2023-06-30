from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printReverse(head):
    # Recursive function to print the linked list in reverse order
    
    # Base case: if head is None, there are no nodes to print
    if head is None:
        return

    # Recursively call printReverse on the next node
    printReverse(head.next)
    
    # Print the data of the current node
    print(head.data, end=" ")

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
            # If head is None, it means the linked list is empty, so assign the newNode as the head and tail
            head = newNode
            tail = newNode

        else:
            # If head is not None, append the newNode to the tail of the linked list
            tail.next = newNode
            tail = newNode

        i += 1

    return head

# To print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()

# Main
t = int(stdin.readline().rstrip())

while t > 0:
    # Take input and create the linked list
    head = takeInput()

    # Print the linked list in reverse order
    printReverse(head)
    print()

    t -= 1
