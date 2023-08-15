def printPairDiffK(l, k):

    dict = {}
    count = 0

    for num in l:
        if k != 0 and  num - k in dict:
            count += dict[num - k]
        
        if num + k in dict:
            count += dict[num + k]

        dict[num] = dict.get(num, 0)+1

    return count 




    
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))
