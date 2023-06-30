# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    # Function to calculate the length of the linked list
    temp = head
    lengthLL = 0
    while temp is not None:
        lengthLL += 1
        temp = temp.next
    return lengthLL

def appendLastNToFirst(head, n):
    # Function to append the last N nodes to the beginning of the linked list
    if n == 0 or head is None or head.next is None:
        # If N is 0 or the list is empty or contains only one node, no modifications needed
        return head
    
    # Calculate the position to remove from the end of the list
    remove = length(head) - n
    count = 1
    curr = head

    # Traverse the list to the (remove-1)th node
    while count < remove:
        curr = curr.next
        count += 1
    
    # Store the (remove-1)th node as 'curr' and the tail of the remaining list as 'tail'
    tail = curr.next
    curr.next = None
    
    # Find the last node of the original list and make it point to the modified list
    temp = tail
    while temp.next is not None:
        temp = temp.next
    
    temp.next = head
    head = tail
    
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
t = int(stdin.readline().rstrip())

while t > 0:
    # Read the number of test cases
    head = takeInput()
    # Read the value of N
    n = int(stdin.readline().rstrip())

    # Append the last N nodes to the beginning of the linked list
    head = appendLastNToFirst(head, n)
    
    # Print the modified linked list
    printLinkedList(head)

    t -= 1
