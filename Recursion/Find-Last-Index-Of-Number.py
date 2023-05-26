from sys import setrecursionlimit
setrecursionlimit(11000)

def lastIndex(arr, x, index):
    if index < 0:
        return -1  # element not found
    elif arr[index] == x:
        return index
    else:
        return lastIndex(arr, x, index - 1)

n = int(input())
arr = list(map(int, input().strip().split(' ')))
x = int(input())
print(lastIndex(arr, x, index=n-1))
