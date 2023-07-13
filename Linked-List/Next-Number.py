## Read input as specified in the question.
## Print output as specified in the question.
# Problem ID 328 Midpoint LL

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def nextNumber(head):
    # This function takes a linked list as input and returns the next number in the sequence.
    # If the current number is 9, then the next number is 1.
    # If the current number is less than 9, then the next number is the current number + 1.

    if head.next is None:
        # If the linked list only has one node, then the next number is simply the current number + 1.
        head.data = head.data + 1
        return head

    curr = head
    while curr.next is not None:
        curr = curr.next

    # If the last node is 9, then the next number is 1.
    # Otherwise, the next number is the current number + 1.

    if curr.data == 9:
        if head.data < 9:
            head.data = head.data + 1
            newTemp = head.next
            while newTemp is not None:
                newTemp.data = 0
                newTemp = newTemp.next
        else:
            head.data = 1
            newTemp = head.next
            while newTemp is not None:
                newTemp.data = 0
                newTemp = newTemp.next
            temp = head.next
            newNode = Node(0)
            head.next = newNode
            newNode.next = temp
    else:
        curr.data = curr.data + 1

    return head

def ll(arr):
    # This function creates a linked list from a list of elements.

    if len(arr) == 0:
        return None

    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    # This function prints the elements of a linked list.

    while head is not None:
        print(head.data, end=' ')
        head = head.next
    return

# Main
# Read the link list elements including -1
arr = [int(ele) for ele in input().split()]

# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
head = nextNumber(l)
printll(head)
