# count occurences of number in a list 

def count_nums(arr, target):
    count = 0 
    for num in arr:
        if num == target:
            count += 1 
    
    return count 
    

# testing 
my_list = [2,4,5,6,2,5,6,4,4,3]
my_target = 6
result = count_nums(my_list, my_target)
print(result)