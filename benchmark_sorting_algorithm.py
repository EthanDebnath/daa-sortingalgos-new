import time
import random
import matplotlib.pyplot as plt

# Import sorting functions from their respective files
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort

def benchmark_sort(sort_fn, arr):
    """
    Measure the execution time of a given sorting function.
    
    Args:
    sort_fn (function): The sorting function to benchmark.
    arr (list): The list to sort.
    
    Returns:
    float: The time taken to sort the list in seconds.
    """
    start_time = time.perf_counter()  #Start timer
    sort_fn(arr)                      #Execute the sorting function
    return time.perf_counter() - start_time

#Varied input sizes to benchmark sorting performance, putting varying stresses on system resources
input_sizes = [5, 10, 20, 75, 150, 300, 500, 750, 1200, 1800]



#Number of repetitions to average results for each input size
num_trials = 5

#Dictionary to store average execution times for each sorting algorithms
results = {
    "Selection Sort": [],
    "Insertion Sort": [],
    "Bubble Sort": []
}

for size in input_sizes:
    #Keep cumulative times
    selection_time, insertion_time, bubble_time = 0, 0, 0

    # Repeat the sorting process multiple times to average results
    for _ in range(num_trials):
        #Generate a random list of integers for sorting
        arr = [random.randint(1, 10000) for _ in range(size)]

        # Benchmark the Sorting algos and accumulate time
        arr_copy = arr.copy()
        selection_time += benchmark_sort(selection_sort, arr_copy)

        arr_copy = arr.copy()
        insertion_time += benchmark_sort(insertion_sort, arr_copy)

        arr_copy = arr.copy()
        bubble_time += benchmark_sort(bubble_sort, arr_copy)

    # Compute and store the average execution time for each algorithm
    results["Selection Sort"].append(selection_time / num_trials)
    results["Insertion Sort"].append(insertion_time / num_trials)
    results["Bubble Sort"].append(bubble_time / num_trials)

#Plot the average execution times for all sorting algorithms
plt.figure(figsize=(12, 7))
plt.plot(input_sizes, results["Insertion Sort"], label='Insertion Sort', marker='o', linestyle='--')
plt.plot(input_sizes, results["Selection Sort"], label='Selection Sort', marker='o', linestyle='-')
plt.plot(input_sizes, results["Bubble Sort"], label='Bubble Sort', marker='o', linestyle='-.')
plt.xlabel('Input Size (n)')
plt.ylabel('Average Time (seconds)')
plt.title('Time Benchmark of Insertion Sort, Selection Sort, Bubble Sort')
plt.legend()
plt.grid(True)
plt.show()

