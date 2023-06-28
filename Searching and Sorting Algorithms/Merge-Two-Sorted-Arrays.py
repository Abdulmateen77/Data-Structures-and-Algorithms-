def merge(arr1, n, arr2, m) :
    # Merge two sorted arrays into a single sorted array.

    i = 0
    j = 0
    arr3 = []

    while i < n and j < m:
        # Compare elements from both arrays and add the smaller element to arr3.
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    # Add remaining elements from arr1, if any.
    while i < n:
        arr3.append(arr1[i])
        i += 1

    # Add remaining elements from arr2, if any.
    while j < m:
        arr3.append(arr2[j])
        j += 1

    return arr3


# Taking Input Using Fast I/O
def takeInput():
    # Read input values for an array/list.

    n = int(stdin.readline().rstrip())

    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


# To print the array/list
def printList(arr, n):
    # Print the elements of the array/list.

    for i in range(n):
        print(arr[i], end=" ")

    print()


# Main
t = int(stdin.readline().rstrip())

while t > 0:
    # Process each test case.

    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1
