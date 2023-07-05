from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findNodeRec(head, n):
    # Recursive function to find the index of a node with value n in the linked list
    
    if head is None:
        return -1
    
    if head.data == n:
        return 0

    # Recursively call the function on the next node
    index = findNodeRec(head.next, n)

    if index == -1:
        return -1
    
    # Increment the index by 1 as we move to the next node
    return 1 + index


def takeInput():
    # Function to take input and create a linked list
    
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


# Main
t = int(stdin.readline().rstrip())

while t > 0:
    # Process multiple test cases

    head = takeInput()
    n = int(stdin.readline().rstrip())

    # Find the index of node with value n in the linked list
    print(findNodeRec(head, n))

    t -= 1
