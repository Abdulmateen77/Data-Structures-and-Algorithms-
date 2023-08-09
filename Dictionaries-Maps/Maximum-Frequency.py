def maximumFreq (arr):
    dict = {}
    for num in arr:
        dict[num] = dict.get(num ,0) + 1

    maximum = -1
    for num in arr:
        if dict[num] > maximum:
            maximum = dict[num]
            maxNum = num

    return maxNum


ArrayInput = int(input())
arr = list(int(i) for i in input().strip().split(' ')[:ArrayInput])
print(maximumFreq(arr))
