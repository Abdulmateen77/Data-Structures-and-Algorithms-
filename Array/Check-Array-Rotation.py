def arrayRotateCheck(arr, n):
    #Your code goes here
    for i in range(0,n-1):
        if arr[i] > arr[i+1]:
            return i +1
    return 0
