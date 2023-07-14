# Following is the Node class already written for the Linked List.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    # This function calculates and returns the length of the linked list.
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def deleteNode(head, pos):
    # This function deletes a node at the given position in the linked list.
    # If the position is invalid, it returns the original head.

    if pos < 0 or pos >= length(head):
        return head

    count = 0
    prev = None
    current = head

    while count < pos:
        prev = current
        current = current.next
        count += 1

    if prev is not None:
        prev.next = current.next
    else:
        head = current.next

    return head




# Taking Input Using Fast I/O.
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

# To print the linked list.
def printLinkedList(head):
    # This function prints the elements of the linked list.
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()

# Main.
t = int(stdin.readline().strip())

while t > 0:
    head = takeInput()
    pos = int(stdin.readline().rstrip())

    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1
