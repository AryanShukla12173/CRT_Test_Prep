def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle index
        left_half = arr[:mid]  # Left sub-array
        right_half = arr[mid:]  # Right sub-array

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements from left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy remaining elements from right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr  # Sorted list

# Example Usage
unsorted_list = list(map(int, input("Enter numbers: ").split()))
sorted_list = merge_sort(unsorted_list)
print(f"Sorted List: {sorted_list}")
