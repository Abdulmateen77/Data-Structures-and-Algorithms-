from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      
def midpoint(head):
    # Function to find the midpoint of a linked list
    # Takes the head of the linked list as input

    if head is None:
        return head

    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

def mergeSort(head):
    # Function to perform merge sort on a linked list
    # Takes the head of the linked list as input

    if head is None or head.next is None:
        return head

    mid = midpoint(head)

    second = mid.next
    mid.next = None

    left = mergeSort(head)
    right = mergeSort(second)

    sortedLL = merge(left, right)

    return sortedLL

def merge(head1, head2):
    # Function to merge two sorted linked lists into a single sorted linked list
    # Takes the heads of the two linked lists as input

    if head1 is None:
        return head2
    
    if head2  is None:
        return head1

    if  head1.data < head2.data:
        result = head1
        result.next = merge(head1.next, head2)
    else:
        result = head2
        result.next = merge(head1,head2.next)

    return result

