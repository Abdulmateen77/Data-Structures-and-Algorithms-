from sys import stdin

def longestConsecutiveSubsequence(arr,n): 
    # Write your code here

    Numset = set(arr)
    ans_start = 0
    ans_end = 0
    max_length = 0
    
    for element in arr:
        if element - 1 not in Numset:
            curr_ele = element
            while curr_ele in Numset:
                curr_ele += 1
            
            if curr_ele - element > max_length:
                max_length = curr_ele - element
                ans_start = element
                ans_end = curr_ele - 1
    
    return [ans_start, ans_end]






def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

    
# Main 
arr,n=takeInput()
ans = longestConsecutiveSubsequence(arr,n) 
# This ans array contains two numbers, ie, start and end of longest sequence respectively
print(*ans)
