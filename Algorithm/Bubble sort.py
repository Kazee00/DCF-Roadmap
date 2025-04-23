def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to detect if any swapping happens
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, the array is already sorted
        if not swapped:
            break
    return arr

arr = [9, 7, 5, 3, 1]
sorted_arr = bubble_sort(arr)  # Sort the array
print("Sorted array is:")
for i in range(len(sorted_arr)):
    print("%d" % sorted_arr[i], end=" ")  # Print each element of the sorted array