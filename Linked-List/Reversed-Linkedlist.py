from sys import stdin  # Importing the stdin module to take input from the console
setrecursionlimit(10**6)  # Setting the maximum recursion depth to 10^6

class Node:  # Defining a Node class
    def __init__(self, data):  # Constructor of the Node class
        self.data = data  # Data of the node
        self.next = None  # Next node in the linked list

# Taking Input Using Fast I/O
def takeInput() :
    head = None  # Head of the linked list
    tail = None  # Tail of the linked list

    datas = list(map(int, stdin.readline().rstrip().split(" ")))  # Taking input from the console

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :  # Iterate over the data list
        data = datas[i]  # Get the current data
        newNode = Node(data)  # Create a new node with the current data

        if head is None :  # If the linked list is empty
            head = newNode  # Set the new node as the head
            tail = newNode  # Set the new node as the tail

        else :  # If the linked list is not empty
            tail.next = newNode  # Set the next node of the tail to the new node
            tail = newNode  # Set the new node as the tail

        i += 1


    return head  # Return the head of the linked list


# To print the linked list 
def printLinkedList(head) :

    while head is not None :  # Iterate over the linked list
        print(head.data, end = " ")  # Print the data of the current node
        head = head.next  # Move to the next node

    print()  # Print a newline character


def reverse(head):
    # Write your code here
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


# Main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    
    ans=reverse(head)
    printLinkedList(ans)

    t -= 1 
