def subsetSum(l):
    # Length of the input list
    n = len(l)
    # Dictionary to store cumulative sums and their corresponding indices
    dict = {}
    
    # Variable to store the maximum length of subarray with zero sum
    max_length = 0
    
    # Variable to store the cumulative sum of elements
    cum_sum = 0             

    for i in range(n):
        # Add the current element to the cumulative sum
        cum_sum += l[i]       

        if cum_sum == 0:
            # If cumulative sum becomes zero, update the max_length
            max_length = i + 1 

        elif cum_sum in dict:
            max_length = max(max_length, i - dict[cum_sum])
            # If cumulative sum is already in dict, update max_length if a longer subarray is found

        else:
            # If cumulative sum is not in dict, add it with its index
            dict[cum_sum] = i  
    # Return the maximum length of subarray with zero sum
    return max_length      



# Main
n = int(input())           # Input the size of the list
l = list(map(int, input().strip().split()))  # Input the list elements
print(subsetSum(l))        # Print the result of the subsetSum function
