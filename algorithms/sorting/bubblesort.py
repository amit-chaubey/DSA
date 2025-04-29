# Define : lowest number in the begining and higest number at the end of the list, and repeat the process unless sorted, looping through.

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
def bubble_sort(arr):
	indexing_length = len(arr)-1  # cannt perform the operation to the last number as there is no number to the next.
	sorted = False

	while not sorted:  # using while loop untill the list is sorted
		sorted = True  # assumption that the list is sorted
		for i in range(0, indexing_length):  # iterates over the list to second last element.
			if arr[i] > arr[i+1]:
				sorted = False
				arr[i], arr[i+1] = arr[i+1], arr[i]  # swapping

	return arr

list1 = [random.randint(1,100) for element in range(10)]
print(f'Sorted List: {bubble_sort(list1)}')


end = time.time()
print(f'Execution time: {end - start} sec.')



# Optimised Version code


start = time.time()
def optimised_bubble(arr):
	n = len(arr)
	for passnum in range(n-1, 0, -1):  # Controls how many times the list is passed through, reducing the range in each pass.
		for i in range(passnum):  # Perform the comparision and swap
			if arr[i]> arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]

	return arr

list2 = [random.randint(1,100) for element in range(10)]
print(f'Sorted List: {optimised_bubble(list2)}')

end = time.time()
print(f'Execution time: {end - start} sec.')