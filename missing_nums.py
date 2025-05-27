def find_missing_nums(usr_nums):
    max_num = max(usr_nums)
    # Create a list of all numbers from 1 up to max_num (inclusive)
    nums_gen = list(range(1, max_num + 1)) 
    
    # Create a set from usr_nums for efficient lookup (optional but good practice)
    # Using a set makes 'if num in usr_nums' (or checking if num is in nums_gen after removal) faster for larger lists
    usr_nums_set = set(usr_nums) 
    
    missing_nums = [] # Initialize an empty list to store missing numbers
    
    for num in nums_gen: # Iterate through the complete range of numbers
        if num not in usr_nums_set: # Check if the current number from the full range is NOT in the user's numbers
            missing_nums.append(num) # If it's not there, it's a missing number
            
    return missing_nums # Return the list of all missing 
    

usr_nums = [1,8]
result = find_missing_nums(usr_nums)
print(result)