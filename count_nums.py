def count_all_nums(arr):
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    return counts

# Testing
my_list = [2, 4, 5, 6, 2, 5, 6, 4, 4, 3]
result = count_all_nums(my_list)
print(result)  # Output: {2: 2, 4: 3, 5: 2, 6: 2, 3: 1}