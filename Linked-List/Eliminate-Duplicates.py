# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeDuplicates(head):
    # Function to remove consecutive duplicate values from a sorted singly linked list
    if head is None:
        # If the list is empty, return the head as it is
        return head

    curr = head
    
    while curr.next is not None:
        # Compare the data of the current node with the data of its next node
        if curr.data == curr.next.data:
            # If the data is equal, it means we have consecutive duplicate values
            # Update the 'next' reference of the current node to skip the duplicate node
            curr.next = curr.next.next
        else:
            # If the data is not equal, move the current pointer to the next node
            curr = curr.next
    
    return head

# Taking Input Using Fast I/O
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
            # If the list is empty, assign the new node as both head and tail
            head = newNode
            tail = newNode
        else:
            # Append the new node to the end of the list
            tail.next = newNode
            tail = newNode

        i += 1

    return head

# To print the linked list
def printLinkedList(head):
    # Function to print the elements of the linked list
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

# Main
t = int(stdin.readline().strip())

while t > 0:
    # Read the number of test cases
    head = takeInput()

    # Remove consecutive duplicate values from the linked list
    head = removeDuplicates(head)
    
    # Print the modified linked list
    printLinkedList(head)

    t -= 1
