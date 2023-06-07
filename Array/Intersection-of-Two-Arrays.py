def intersections(arr1, n, arr2, m):
    # Iterate through each element in arr1
    for i in range(n):
        element = arr1[i]
        
        # Iterate through each element in arr2
        for j in range(m):
            # Check if the element from arr1 matches an element in arr2
            if element == arr2[j]:
                # Print the element
                print(element, end=" ")
                
                # Update the corresponding element in arr2 to mark it as visited
                arr2[j] = -2
                
                # Exit the inner loop to avoid duplicate matches
                break
