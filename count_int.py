from collections import Counter

lst = [2,2,4,1,5,2,7,3,9,6,3,4,8,7,6,4,9,3,5,9]

counters = Counter(lst)

for key, value in counters.items():
    print(f"the count of number {key}: {value}")

