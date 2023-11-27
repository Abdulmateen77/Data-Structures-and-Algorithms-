#Initialize the function that calculates the minimum time to assemble a car
def solution(A, B, X, Y):
    #Get the number of cars to assemble
    number_of_cars = len(A)

    #Create a matrix to store the minimum time to reach each position on both lines
    dp = [[float('inf')] * 2 for _ in range(number_of_cars)]

    #Initialize the first position on both lines
    dp[0][0] = A[0]
    dp[0][1] = B[0]

    #Fill in the matrix based on the minimum time to reach each position
    for position in range(1, number_of_cars):
        dp[position][0] = min(dp[position-1][0] + A[position], dp[position-1][1] + A[position] + Y)
        dp[position][1] = min(dp[position-1][1] + B[position], dp[position-1][0] + B[position] + X)

    #Return the minimum time to assemble the entire car
    return min(dp[number_of_cars-1][0], dp[number_of_cars-1][1])

#Examples:
#Test case where assembly can start in line A, switching between lines when necessary
result1 = solution([1, 6, 2], [3, 2, 5], 2, 1)

 #Test case where it is optimal to assemble the entire car on line A
result2 = solution([2, 11, 4, 4], [9, 2, 5, 11], 8, 4)

#Test case with a different set of parameters
result3 = solution([1, 10, 1], [10, 1, 10], 1, 5)

#Another test case with different parameters
result4 = solution([8, 3, 3], [6, 1, 10], 4, 3)

# Print the results of the test cases
print(result1)  # Output: 8
print(result2)  # Output: 21
print(result3)  # Output: 9
print(result4)  # Output: 13
