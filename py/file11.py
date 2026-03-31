"""11-vazifa: Bo'lin va zabt et usuli bilan massivdagi inversiyalar sonini hisoblash.

Inversiya — bu i < j indekslar juftligi bo'lib, arr[i] > arr[j].
Merge sort asosida O(n log n) yechim.
"""


def count_inversions(arr):
    """Inversiyalar sonini va saralangan massivni qaytaradi."""
    if len(arr) <= 1:
        return arr[:], 0

    mid = len(arr) // 2
    left, left_inv = count_inversions(arr[:mid])
    right, right_inv = count_inversions(arr[mid:])

    merged = []
    inversions = left_inv + right_inv
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions


if __name__ == "__main__":
    test_cases = [
        [2, 4, 1, 3, 5],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
    ]
    for arr in test_cases:
        _, inv_count = count_inversions(arr)
        print(f"Massiv: {arr}  ->  Inversiyalar soni: {inv_count}")