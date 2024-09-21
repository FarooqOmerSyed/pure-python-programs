def is_pronic(number):
    i = 0
    while i * (i + 1) <= number:
        if i * (i + 1) == number:
            return True
        i += 1
    return False

# Test the function
print(is_pronic(6))  # Output: True (6 = 2 * 3)
print(is_pronic(20))  # Output: True (20 = 4 * 5)
print(is_pronic(7))  # Output: False
