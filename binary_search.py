def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoids potential overflow
        
        # Check if the target is present at mid
        if arr[mid] == target:
            return mid  # Target found
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1
            
    return -1  # Target not found

# Example usage
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(sorted_list, target)

if result != -1:
    print(f"Element found at index {result} 🎉")
else:
    print("Element not found! ❌")
