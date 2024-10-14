# Merge Sort Implementation
# Problem: Implement the merge sort algorithm to sort an array of integers.
# Objective: Learn and practice an advanced sorting algorithm with O(n log n) time complexity.

# Merge Sort Algorithm

def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point
        mid = len(arr) // 2
        
        # Divide the array elements into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merge the two sorted halves
        i = j = k = 0
        
        # Copy data to temporary arrays L[] and R[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)
