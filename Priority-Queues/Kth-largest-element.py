import heapq
def kthLargest(lst, k):
    heap = lst[0:k]
    heapq.heapify(heap)

    for num in lst[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,num)
    
    return heap[0]




# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)
