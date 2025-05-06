# print("Hello World")
# This is a simple Python script to demonstrate time complexity

# 🔹 Common Big O Notations (Time Complexity):

# Big O	Description	Example

# O(n)	          Constant time	            Accessing an element by index
# O(log n)	      Logarithmic time	        Binary search
# O(n)	          Linear time	              Loop through an array
# O(n log n)	    Linearithmic time	        Merge sort, Quick sort (average case)
# O(n²)         	Quadratic time	          Nested loops over an array
# O(2ⁿ)         	Exponential time	        Solving problems with brute-force recursion (like subsets)
# O(n!)         	Factorial time	          Solving the Traveling Salesman Problem (TSP) brute-force


# O(n)	          Constant time	            Accessing an element by index
def print_items(arr):
    for item in arr:
        print(item)
  
arr = [1, 2, 3, 4, 5]
# print_items(arr)

# O(n**2)	        Logarithmic time	        Binary search
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)

arr = [1, 2, 3, 4, 5]

print_pairs(arr)

########################################
def linear_time(arr):
    return arr[0]



### O(log n) – Logarithmic Time Complexity
# Logarithmic time complexity occurs when the algorithm reduces the problem size by a constant factor (usually 2) at each step.
# This is common in algorithms that divide the input in half, such as binary search. [Searching algorithms]
def log_time_example(n):
    while n > 1:
        print(n)
        n = n // 2


######### O(n log n) – Linearithmic Time Complexity
# Linearithmic time complexity is often seen in algorithms that perform a logarithmic operation for each element in the input.
# A common example is the merge sort algorithm, which divides the array in half (log n) and then merges the sorted halves (n). [Sorting algorithms]
def log_n_example(n):
    if n <= 1:
        return
    mid = n // 2
    log_n_example(mid)
    log_n_example(n - mid)
    for i in range(n):  # O(n)
        pass


## O(n!) – Factorial Time Complexity
# Factorial time complexity is seen in algorithms that generate all permutations of a set. The number of permutations of n items is n! (n factorial).
# This is extremely inefficient for large n, as the number of permutations grows very quickly.
def permutations(s):
    if len(s) <= 1:
        return [s]
    result = []
    for i in range(len(s)):
        rest = s[:i] + s[i+1:]
        for p in permutations(rest):
            result.append(s[i] + p)
    return result


### O(2ⁿ) – Exponential Time Complexity
# Exponential time complexity occurs when the algorithm's growth doubles with each addition to the input size.
# This is common in algorithms that solve problems by exploring all possible combinations, such as the recursive solution to the Fibonacci sequence.
# This is extremely inefficient for large n, as the number of combinations grows very quickly.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
