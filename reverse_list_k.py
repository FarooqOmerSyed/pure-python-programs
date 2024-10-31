# rotate a list from k position 

def rotate_list(arr, k):
    if len(arr) <= k:
        print(f"the k value should be less than {k}")
    for i, j in enumerate(arr):
        if i == k:
            return arr + arr[k:]
    

my_arr = [1,2,34,5,6,7]
my_k = 2 
result = rotate_list(my_arr, my_k)
print(result)

