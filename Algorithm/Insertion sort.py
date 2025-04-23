def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr  # Return the sorted array after the loop completes

arr = [5, 3, 8, 6, 2]
sorted_arr = insertion_sort(arr)  # Sort the array
print("Sorted array is:")
for i in range(len(sorted_arr)):
    print("%d" % sorted_arr[i], end=" ")  # Print each element of the sorted array