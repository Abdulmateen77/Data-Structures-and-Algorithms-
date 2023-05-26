def firstIndex(arr, x, index = 0):
    # Please add your code here
    
    if index == len(arr):
        return -1
    elif arr[index] == x:
        return index
    else:
        return firstIndex(arr, x, index + 1)
    

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x,index = 0))
