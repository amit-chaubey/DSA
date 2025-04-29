"""
Utility module for measuring execution time of algorithms and data structure operations.
"""

import time
from functools import wraps
from typing import Any, Callable, TypeVar, cast

T = TypeVar('T')

def measure_time(func: Callable[..., T]) -> Callable[..., T]:
    """
    A decorator that measures and prints the execution time of a function.
    
    Args:
        func: The function to measure
        
    Returns:
        The wrapped function that prints execution time
        
    Example:
        @measure_time
        def my_function():
            # function code here
            pass
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} execution time: {end_time - start_time:.6f} seconds")
        return result
    return cast(Callable[..., T], wrapper)

def benchmark(func: Callable[..., Any], *args: Any, iterations: int = 1000, **kwargs: Any) -> float:
    """
    Benchmark a function by running it multiple times and returning average execution time.
    
    Args:
        func: The function to benchmark
        *args: Positional arguments to pass to the function
        iterations: Number of times to run the function (default: 1000)
        **kwargs: Keyword arguments to pass to the function
        
    Returns:
        Average execution time in seconds
        
    Example:
        avg_time = benchmark(my_sort_function, my_list, iterations=100)
    """
    total_time = 0
    
    for _ in range(iterations):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        total_time += end_time - start_time
        
    avg_time = total_time / iterations
    print(f"Average execution time over {iterations} iterations: {avg_time:.6f} seconds")
    return avg_time 