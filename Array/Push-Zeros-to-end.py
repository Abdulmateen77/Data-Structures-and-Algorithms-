# Find the first occurrence of zero
for i in range(n):
    if arr[i] == 0:
        j = i
        break

# If no zeros found, return the original array
if j == -1:
    return arr

# Move non-zero elements to the left of zeros
for i in range(j+1, n):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1

return arr
