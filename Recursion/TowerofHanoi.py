def towerofhanoi(n, source, aux, dest):
    # Base case: If n is 0, there are no disks to move, so return
    if n == 0:
        return
    
    # Base case: If n is 1, move the disk from source to destination
    elif n == 1:
        print(source + " " + dest)
        return
    
    # Recursive case:
    # Move (n-1) disks from source to auxiliary tower, using the destination tower as the auxiliary tower
    towerofhanoi(n - 1, source, dest, aux)
    
    # Move the nth disk from source to destination
    print(source + " " + dest)
    
    # Move (n-1) disks from auxiliary tower to destination tower, using the source tower as the auxiliary tower
    towerofhanoi(n - 1, aux, source, dest)


n = int(input())  # Read the number of disks
towerofhanoi(n, 'a', 'b', 'c')  # Call the towerofhanoi function with the initial setup
