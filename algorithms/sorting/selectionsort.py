
# Define: This alogrim find the minimum value in the list, by picking the first number and comparing each number to the right , as soon as we get the minimum number, we can assign it to new mininum number, and loop through the rest of number, we can divide the list into two, sorted and unsorted.

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


start_time = time.time()
def selection_sort(arr):
	"""Define that takes a list and sort using selection operation."""

	for i in  range(0 , len(arr)-1):
		min_value = i  # indicates statering point of unsorted section of the list.


		for j in range(i+1, len(arr)):
			if arr[j] < arr[min_value]:
				min_value = j
        # Swap the found minimum element with the first element
		if min_value != i:
			arr[min_value], arr[i] = arr[i], arr[min_value]


	return arr


# let's test the function
list_a1 = [random.randint(1,100) for element in range(10)]
print(f'Selection Sorted List: {selection_sort(list_a1)}')

end_time = time.time()

print(f'Execution time: {end_time - start_time} sec.')


# Relatively Efficient method

def selection_sort(arr):
	"""Define that takes a list and sort using selection operation."""

	for i in range(len(arr)-1):
		min_value = i  # indicates statering point of unsorted section of the list.

		for j in range(i+1, len(arr)):
			if arr[j] < arr[min_value]:
				min_value = j
        # Swap the found minimum element with the first element
		if min_value != i:
			arr[min_value], arr[i] = arr[i], arr[min_value]


	return arr


# let's test the function
list2 = [random.randint(1,100) for element in range(10)]
print(f'Selection Sorted List: {selection_sort(list2)}')

end_time = time.time()

print(f'Execution time: {end_time - start_time} sec.')
