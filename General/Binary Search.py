def binarySearch(arr, x):
    start = 0
    end = len(arr)
    while start <= end:
        mid = start + (end-start)//2
        if x < arr[mid]:
            end = mid - 1
        elif x > arr[mid]:
            start = mid + 1
        else:
            return True
    return False

