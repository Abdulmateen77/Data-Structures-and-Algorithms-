def maximumProfit(arr):
# Function to find the maximum profit that can be obtained from selling items with given prices
# arr: list of prices

arr.sort()  # Sort the prices in ascending order

n = len(arr)
max_profit = 0

# Calculate revenue for each price and update the maximum profit
for i in range(n):
    revenue = arr[i] * (n - i)
    max_profit = max(max_profit, revenue)

return max_profit
n = int(input()) # Read the number of prices
arr = [int(ele) for ele in input().split()] # Read the prices as a list

ans = maximumProfit(arr) # Call the maximumProfit function to find the maximum profit

print(ans) # Print the maximum profi
