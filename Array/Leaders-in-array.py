def leaders(arr, N):
    max_so_far = arr[N - 1]  # Initialize the maximum element as the last element of the array
    leader_list = [max_so_far]  # Create a list to store the leaders
    for i in range(N-2, -1, -1):
        # Traverse the array from right to left
        # Check if the current element is greater than or equal to the maximum element so far
        if arr[i] >= max_so_far:
            max_so_far = arr[i]  # Update the maximum element
            leader_list.append(max_so_far)  # Add the current element to the leader list
    leader_list.reverse()  # Reverse the leader list to get the correct order
    return leader_list  # Return the list of leaders

