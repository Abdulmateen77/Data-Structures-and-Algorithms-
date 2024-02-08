def arrayEquilibriumIndex(arr, n):
#Function to find the equilibrium index of an array
# arr: input array
# n: length of the array

totalSum = 0  # Variable to store the total sum of array elements

#Calculate the total sum of array elements
for i in range(n):
    totalSum += arr[i]

leftSum = 0  # Variable to store the left sum of elements
index = 0  # Variable to store the current index

#Iterate through the array to find the equilibrium index
while index < n:
    rightSum = totalSum - leftSum - arr[index]
    
    if rightSum == leftSum:
        # If the right sum and left sum are equal, return the current index
        return index
    else:
        #Update the left sum and move to the next index
        leftSum += arr[index]
        index += 1

return -1  #Return -1 if no equilibrium index is found
