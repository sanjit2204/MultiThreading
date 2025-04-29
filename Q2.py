import threading
import time
import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def single_threaded_quicksort(arr):
    arr_copy = arr.copy()
    quicksort(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy

def threaded_quicksort(arr, low, high, depth=0, max_depth=3):
    if low < high:
        if depth >= max_depth or high - low < 1000:
            quicksort(arr, low, high)
            return

        pivot_index = partition(arr, low, high)

        left_thread = threading.Thread(
            target=threaded_quicksort,
            args=(arr, low, pivot_index - 1, depth + 1, max_depth)
        )

        left_thread.start()

        threaded_quicksort(arr, pivot_index + 1, high, depth + 1, max_depth)

        left_thread.join()

def multi_threaded_quicksort(arr, max_depth=3):
    arr_copy = arr.copy()
    threaded_quicksort(arr_copy, 0, len(arr_copy) - 1, 0, max_depth)
    return arr_copy

def compare_quicksorts(arr_size=10000, max_depth=3):
    arr = [random.randint(1, 100000) for _ in range(arr_size)]
    print(f"Array size: {arr_size}")
    print(f"Max thread depth: {max_depth}")

    start_time = time.time()
    single_sorted = single_threaded_quicksort(arr)
    single_time = time.time() - start_time
    print(f"Single-threaded time: {single_time:.4f} seconds")

    start_time = time.time()
    multi_sorted = multi_threaded_quicksort(arr, max_depth)
    multi_time = time.time() - start_time
    print(f"Multi-threaded time: {multi_time:.4f} seconds")

    print(f"Results match: {single_sorted == multi_sorted}")
    if multi_time > 0:
        print(f"Speedup: {single_time / multi_time:.2f}x")
    print("-" * 40)

if __name__ == "__main__":
    example_array = [21, 5, 17, 8, 99, 33, 1, 76]
    print("Original array:", example_array)
    sorted_example = multi_threaded_quicksort(example_array)
    print("Sorted array:", sorted_example)
    print()

    for size in [1000, 10000, 100000, 1000000]:
        try:
            compare_quicksorts(size)
            print()
        except Exception as e:
            print(f"Error with size {size}: {e}")
            print()
