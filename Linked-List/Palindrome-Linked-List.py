from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)

#Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def isPalindrome(head):
    if head is None or head.next is None:
        return True

    # Find the middle of the linked list
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    second_half = slow.next
    slow.next = None

    # Reverse the second half of the linked list
    prev = None
    curr = second_half

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    second_half = prev

    # Compare the first half and reversed second half
    first_half = head

    while second_half is not None:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True

#Taking Input Using Fast I/O
def takeInput():
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

#to print the linked list 
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()

#main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    
    if isPalindrome(head):
        print('true')
    else:
        print('false')
        
    t -= 1
