def sumArray(arr,length):
    # Please add your code here
    if length <= 0:
        return 0
    else:
        return sumArray(arr,length-1) + arr[length-1]


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
length = len(arr)
print(sumArray(arr,length))
