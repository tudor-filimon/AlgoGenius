
def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Test cases and execution
test_cases = [
    [64, 25, 12, 22, 11],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [2, 2, 2, 2, 2],
    []
]

# Print results
for idx, tc in enumerate(test_cases):
    sorted_array = selection_sort(tc[:])
    print(f"Test case {idx+1}: Original array: {tc}, Sorted array: {sorted_array}")
