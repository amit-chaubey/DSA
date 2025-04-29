# Define: take a unsorted list and divide into sorted and unsorted list, and then moving the unsorted number once found to the sorted list

# O(n!) - Factorial Time: Extremely inefficient, with complexity increasing factorially based on the size of the input data (e.g., certain brute-force algorithms).

# O(2^n) - Exponential Time: Complexity doubles with each addition to the input data set. This is typical of algorithms that solve problems via recursion, such as the classic Fibonacci sequence calculation.

# O(n^k) - Polynomial Time: The complexity is a polynomial function of the input size. This is better than exponential but can still be quite inefficient for large inputs.

# O(n^3) - Cubic Time: Specific case of polynomial time where the complexity is proportional to the cube of the size of the input data.

# O(n^2) - Quadratic Time: Algorithms with quadratic complexity increase the execution time quadratically with an increase in the input data size (e.g., certain sorting algorithms like bubble sort).

# O(n log n) - Linearithmic Time: More efficient than quadratic algorithms, commonly found in efficient sorting algorithms like mergesort and heapsort.

# O(n) - Linear Time: Complexity grows linearly and in direct proportion to the size of the input data (e.g., simple loops over an array).

# O(log n) - Logarithmic Time: The complexity grows logarithmically with the input size. This is very efficient for large datasets (e.g., binary search).

# O(1) - Constant Time: The most efficient complexity, where the time required to execute an algorithm is constant and does not depend on the size of the input data (e.g., accessing an element in an array by index).



import random
import time


start = time.time()

def insertion_sort(arr):
	for i in range(1, len(arr)):
		value_to_sort = arr[i]

		while arr[i-1] > value_to_sort and i>0:
			arr[i], arr[i-1] = arr[i-1], arr[i]
			i = i-1

	return arr

print(f'Inserted Sorted List: {insertion_sort([random.randint(1,100) for element in range(10)])}')

end = time.time()
print(f'Execution time: {end - start} sec.')


start = time.time()

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[i]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = arr[i]
    return arr


print(f'Inserted Sorted List: {insertion_sort([random.randint(1,100) for element in range(10)])}')

end = time.time()
print(f'Execution time: {end - start} sec.')