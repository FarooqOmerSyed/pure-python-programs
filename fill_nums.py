# given a list of two numbers, only between 1 and 9, create/fill the new \
# list with missing numbers.

def fill_missing_nums(usr_lst):
    max_num = max(usr_lst)
    num_gen = list(range(1, max_num+1))
    merge_nums = usr_lst + num_gen
    remove_duplicates = set(merge_nums)
    result = list(remove_duplicates)
    print(result)

usr_lst = [5,9]
fill_missing_nums(usr_lst)