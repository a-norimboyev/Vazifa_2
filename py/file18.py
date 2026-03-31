"""18-vazifa: Quick Select yordamida k-nchi eng kichik elementni topish.

Bo'lish va zabt etish (Lomuto partition) asosida O(n) o'rtacha.
"""

import random


def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]

    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


def quick_select(arr, k):
    """k-nchi eng kichik elementni topadi (1-indexed)."""
    if k < 1 or k > len(arr):
        raise ValueError("k massiv chegarasidan tashqarida")

    data = arr[:]
    low, high = 0, len(data) - 1
    target = k - 1

    while low <= high:
        pivot_pos = partition(data, low, high)
        if pivot_pos == target:
            return data[pivot_pos]
        elif pivot_pos < target:
            low = pivot_pos + 1
        else:
            high = pivot_pos - 1

    return None


if __name__ == "__main__":
    test_arr = [7, 10, 4, 3, 20, 15]
    print(f"Massiv: {test_arr}")

    for k in range(1, len(test_arr) + 1):
        result = quick_select(test_arr, k)
        print(f"  {k}-nchi eng kichik element: {result}")
