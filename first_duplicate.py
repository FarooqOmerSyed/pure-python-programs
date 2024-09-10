def first_duplicate(lst):
    seen = set()
    for num in lst:
        if num in seen:
            print(f"{num} is the first duplicate")
            return num 
        seen.add(num)
    print(f"No duplicates found!")
    return None
    
my_list = [3, 1, 4, 2, 5, 3]
my_list2 = [3, 1, 4, 2, 5, 6]
result = first_duplicate(my_list)
result2 = first_duplicate(my_list2)

