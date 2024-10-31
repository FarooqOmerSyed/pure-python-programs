def rotate_list(arr, k):
    """Rotates a list to the right by k positions.

    Args:
        arr: The input list.
        k: The number of positions to rotate.

    Returns:
        The rotated list.
    """
    n = len(arr)
    if n == 0:
        return arr  # Return the same list if it's empty
    
    k = k % n  # Normalize k to avoid extra rotations
    return arr[-k:] + arr[:-k]  # Concatenate the last k elements with the rest

# Example usage:
if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5]
    k = 2
    rotated_list = rotate_list(input_list, k)
    print("Original list:", input_list)
    print("Rotated list:", rotated_list)
