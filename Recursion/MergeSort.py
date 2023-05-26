def merge_sort(arr):
    # Base case: if the length of the array is less than or equal to 1, return
    if len(arr) <= 1:
        return

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    # Recursive calls to sort the left and right halves of the array
    merge_sort(left)
    merge_sort(right)

    # Merge the sorted left and right halves
    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    # Merge the two sorted lists a and b into arr
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    # Copy any remaining elements from list a
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    # Copy any remaining elements from list b
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == '__main__':
    nums = [
        [5, 2, 3, 1],
        [5, 1, 1, 2, 0, 0]
    ]

    for arr in nums:
        merge_sort(arr)
        print(arr)
