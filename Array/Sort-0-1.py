from sys import stdin

def sortZeroesAndOne(arr, n):
    s = 0  # Start pointer
    e = n - 1  # End pointer
    
    while s <= e:
        if arr[s] == 0:
            s += 1  # Increment start pointer if the element is 0
        else:
            arr[s], arr[e] = arr[e], arr[s]  # Swap the elements at start and end pointer if the element is 1
            e -= 1  # Decrement end pointer

# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

def printList(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()

# Main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    print()
    t -= 1
