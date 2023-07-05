from sys import stdin

# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def evenAfterOdd(head):
    # Your code goes here
    if head is None or head.next is None:
        return head
    
    oddHead = None
    oddTail = None
    evenHead = None
    evenTail = None

    current = head

    while current is not None:
        if current.data % 2== 0:
            # Append even node to the even list
            if evenHead is None:
                evenHead = current
                evenTail = current
            else:
                evenTail.next = current
                evenTail = current
        else:
            # Append odd node to the odd list
            if oddHead is None:
                oddHead = current
                oddTail = current
            else:
                oddTail.next = current
                oddTail = current

        current = current.next

    # Connect the odd and even lists
    if oddHead is None:
        return evenHead
    else:
        oddTail.next = evenHead

    if evenTail is not None:
        evenTail.next = None

    return oddHead


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


# Function to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# Main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)

    t -= 1
