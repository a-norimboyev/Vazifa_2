"""6-vazifa: turli pivot strategiyalari bilan tezkor saralash."""

import random
import time


def choose_pivot_index(arr, low, high, strategy):
    if strategy == "first":
        return low
    if strategy == "last":
        return high
    if strategy == "middle":
        return (low + high) // 2
    if strategy == "random":
        return random.randint(low, high)
    raise ValueError("Noma'lum pivot strategiyasi")


def partition(arr, low, high, strategy):
    pivot_index = choose_pivot_index(arr, low, high, strategy)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low=0, high=None, strategy="last"):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high, strategy)
        quick_sort(arr, low, pi - 1, strategy)
        quick_sort(arr, pi + 1, high, strategy)


def compare_pivot_strategies(data):
    for strategy in ["first", "last", "middle", "random"]:
        arr_copy = data[:]
        start = time.perf_counter()
        quick_sort(arr_copy, strategy=strategy)
        elapsed = time.perf_counter() - start
        print(f"{strategy:>6} pivot -> {elapsed:.6f} soniya")


if __name__ == "__main__":
    sample = [random.randint(1, 10000) for _ in range(2000)]
    compare_pivot_strategies(sample)