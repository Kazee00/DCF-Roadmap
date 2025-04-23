def Merge(Arr, start, mid, end):
    temp = [0] * (end - start + 1)
    i = start
    j = mid + 1
    k = 0

    while i <= mid and j <= end:
        if Arr[i] <= Arr[j]:
            temp[k] = Arr[i]
            i += 1
        else:
            temp[k] = Arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = Arr[i]
        i += 1
        k += 1

    while j <= end:
        temp[k] = Arr[j]
        j += 1
        k += 1

    for p in range(len(temp)):
        Arr[start + p] = temp[p]

def MergeSort(Arr, start, end):
    if start < end:
        mid = (start + end) // 2
        MergeSort(Arr, start, mid)
        MergeSort(Arr, mid + 1, end)
        Merge(Arr, start, mid, end)

# Example usage
Arr = [6, 5, 12, 10, 9, 1]
MergeSort(Arr, 0, len(Arr) - 1)
print("Sorted array:", Arr)