def swap(array, i, j):
    # Swap two elements in the array
    array[i], array[j] = array[j], array[i]

def partition(array, start, end):
    # Choose the middle element as the pivot
    pivot = array[(start + end) // 2]
    i = start
    j = end

    while i <= j:
        # Move the left pointer to the right until a value larger than the pivot is found
        while array[i] < pivot:
            i += 1
        # Move the right pointer to the left until a value smaller than the pivot is found
        while array[j] > pivot:
            j -= 1
        # Swap elements if the left pointer is still before the right pointer
        if i <= j:
            swap(array, i, j)
            i += 1
            j -= 1

    # Return the position where the left pointer stopped
    return i

def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    if start < end:
        # Partition the array and get the index where the left pointer stopped
        pivot_idx = partition(array, start, end)

        # Recursively sort the left half
        quick_sort(array, start, pivot_idx - 1)
        # Recursively sort the right half
        quick_sort(array, pivot_idx, end)

    return array

array =[3,62,5,5,4,7]
print(quick_sort(array))