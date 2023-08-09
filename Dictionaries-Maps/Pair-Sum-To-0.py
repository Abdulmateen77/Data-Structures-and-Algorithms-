from sys import stdin

def pairSum0(l,n):
    sum=0
    count=0
    map={ }
    for i in range(n):
        if sum-arr[i] in map:
            count+=map[sum-arr[i]]
        if arr[i] in map:
            map[arr[i]]+=1
        else:
            map[arr[i]]=1
    return count


    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))
