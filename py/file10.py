"""10-vazifa: turli algoritmlar ishlashini jadvalda taqqoslash."""

import random
import time


def bubble_sort(arr):
    result = arr[:]
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def selection_sort(arr):
    result = arr[:]
    n = len(result)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    return result


def insertion_sort(arr):
    result = arr[:]
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def quick_sort(arr):
    result = arr[:]

    def _quick(low, high):
        if low >= high:
            return
        pivot = result[(low + high) // 2]
        i, j = low, high
        while i <= j:
            while result[i] < pivot:
                i += 1
            while result[j] > pivot:
                j -= 1
            if i <= j:
                result[i], result[j] = result[j], result[i]
                i += 1
                j -= 1
        _quick(low, j)
        _quick(i, high)

    _quick(0, len(result) - 1)
    return result


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def list_to_linked(values):
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def linked_to_list(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values


def split(head):
    if head is None or head.next is None:
        return head, None
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    return head, mid


def merge(left, right):
    dummy = Node(0)
    tail = dummy
    while left and right:
        if left.value <= right.value:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    tail.next = left if left else right
    return dummy.next


def linked_merge_sort(head):
    if head is None or head.next is None:
        return head
    left, right = split(head)
    return merge(linked_merge_sort(left), linked_merge_sort(right))


def merge_sort_linked_wrapper(arr):
    head = list_to_linked(arr)
    sorted_head = linked_merge_sort(head)
    return linked_to_list(sorted_head)


def insertion_sort_range(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def hybrid_sort(arr, threshold=10):
    result = arr[:]

    def _hybrid(low, high):
        if low >= high:
            return
        if high - low + 1 < threshold:
            insertion_sort_range(result, low, high)
            return
        pivot = result[high]
        i = low - 1
        for j in range(low, high):
            if result[j] <= pivot:
                i += 1
                result[i], result[j] = result[j], result[i]
        result[i + 1], result[high] = result[high], result[i + 1]
        pi = i + 1
        _hybrid(low, pi - 1)
        _hybrid(pi + 1, high)

    _hybrid(0, len(result) - 1)
    return result


def generate_case(size, case_type):
    if case_type == "tasodifiy":
        return [random.randint(0, size * 10) for _ in range(size)]
    if case_type == "saralangan":
        return list(range(size))
    if case_type == "teskari":
        return list(range(size, 0, -1))
    raise ValueError("Noma'lum holat")


def benchmark(algorithms, sizes, cases):
    print(
        f"{'Algoritm':<18} {'Olcham':<8} {'Holat':<10} {'Vaqt (s)':<10}"
    )
    print("-" * 52)

    for size in sizes:
        for case_name in cases:
            base = generate_case(size, case_name)
            for name, func in algorithms.items():
                test_data = base[:]
                start = time.perf_counter()
                sorted_data = func(test_data)
                elapsed = time.perf_counter() - start

                if sorted_data != sorted(base):
                    raise RuntimeError(f"{name} noto'g'ri saraladi")

                print(f"{name:<18} {size:<8} {case_name:<10} {elapsed:<10.6f}")


if __name__ == "__main__":
    algorithms = {
        "Bubble": bubble_sort,
        "Selection": selection_sort,
        "Insertion": insertion_sort,
        "Quick": quick_sort,
        "MergeLinked": merge_sort_linked_wrapper,
        "Hybrid": hybrid_sort,
    }
    benchmark(
        algorithms,
        sizes=[100, 1000, 10000],
        cases=["tasodifiy", "saralangan", "teskari"],
    )