"""9-vazifa: gibrid saralash (quick sort + insertion sort)."""


def insertion_sort_range(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def hybrid_sort(arr, low=0, high=None, threshold=10):
    if high is None:
        high = len(arr) - 1

    if low >= high:
        return arr

    if high - low + 1 < threshold:
        insertion_sort_range(arr, low, high)
    else:
        pi = partition(arr, low, high)
        hybrid_sort(arr, low, pi - 1, threshold)
        hybrid_sort(arr, pi + 1, high, threshold)

    return arr


if __name__ == "__main__":
    nums = [12, 11, 13, 5, 6, 7, 4, 15, 2, 9, 1]
    print("Boshlang'ich:", nums)
    print("Gibrid saralangan:", hybrid_sort(nums[:]))