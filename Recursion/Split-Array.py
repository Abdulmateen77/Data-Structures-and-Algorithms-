def split(arr, i, sum):
# Function to check if the array can be split into two subsets with equal sum
# arr: list of integers
# i: current index in the array
# sum: current sum of elements in the subset

if i == len(arr):
    # Base case: reached the end of the array
    if sum == 0:
        return True
    else:
        return False

if arr[i] % 5 == 0:
    # If the current element is divisible by 5, include it in the sum
    return split(arr, i + 1, sum + arr[i])
elif arr[i] % 3 == 0:
    # If the current element is divisible by 3, subtract it from the sum
    return split(arr, i + 1, sum - arr[i])
else:
    # Try including and excluding the current element and check for both cases
    ans1 = split(arr, i + 1, sum + arr[i])
    ans2 = split(arr, i + 1, sum - arr[i])
    return ans1 or ans2
n = int(input()) # Read the number of elements in the array
arr = [int(ele) for ele in input().split()] # Read the elements of the array

ans = split(arr, 0, 0) # Call the split function to check if array can be split

if ans is True:
print('true')
else:
print('false')
