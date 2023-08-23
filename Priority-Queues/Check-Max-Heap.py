def checkMaxHeap(lst):

    n = len(lst)

    for i in range(n-1):
        if lst[i] > lst[i+1]:
            continue
        
        else:
            return False
    
    return True

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')
