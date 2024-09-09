def max_product_two(lst):
    lst.sort()  # Sort the list in place
    result = lst[-2] * lst[-1]  # Multiply the two largest numbers
    return result  

nums = [3, 6, 1, 4, 2, 5]
multiply = max_product_two(nums)
print(multiply)