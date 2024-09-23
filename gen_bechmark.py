import timeit

def num_gen(n):
    for i in range(n):
        yield i 

def collect_numbers():
    result = []
    for num in num_gen(9):
        result.append(num)
    return result

# Benchmark the collect_numbers function
execution_time = timeit.timeit(collect_numbers, number=10000)
print(f"Execution time for 10,000 runs: {execution_time:.2f} seconds")
