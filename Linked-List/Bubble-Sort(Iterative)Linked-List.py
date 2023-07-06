from sys import stdin

# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def bubbleSort(head):
    # If the list is empty or contains only one element, it is already sorted
    if head is None or head.next is None:
        return head

    swapped = True
    while swapped:
        swapped = False
        previous = None
        current = head

        # Iterate through the list
        while current.next is not None:
            next_node = current.next
            if current.data > next_node.data:
                # Swap current and next_node
                if previous is not None:
                    previous.next = next_node
                else:
                    head = next_node

                current.next = next_node.next
                next_node.next = current

                previous = next_node
                swapped = True
            else:
                previous = current
                current = next_node

    return head


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


def printLinkedList(head):
    # Traverse the linked list and print the values
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# Main function
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)
