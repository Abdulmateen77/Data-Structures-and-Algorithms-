def subsetSum(l):

    n = len(l)
    dict = {}
    max_length = 0
    cum_sum = 0

    for i in range(n):
        cum_sum += l[i]

        if cum_sum == 0:
            max_length = i + 1
        
        elif cum_sum in dict:
            max_length = max(max_length, i - dict[cum_sum])
        
        else:
            dict[cum_sum] = i
    
    return max_length



# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))
