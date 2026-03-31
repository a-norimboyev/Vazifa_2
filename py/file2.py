"""2-vazifa: saralangan massivda elementning barcha indekslari (ikkilik qidiruv)."""


def binary_search_all_indices(arr, target):
    """Target barcha uchragan indekslarini qaytaradi. Massiv saralangan bo'lishi kerak."""
    left, right = 0, len(arr) - 1
    first = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            first = mid
            right = mid - 1

    if first == -1:
        return []

    left, right = first, len(arr) - 1
    last = first
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            last = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return list(range(first, last + 1))


if __name__ == "__main__":
    nums = [1, 2, 2, 2, 3, 4, 5, 5]
    x = 2
    print(f"Massiv: {nums}")
    print(f"{x} uchun barcha indekslar: {binary_search_all_indices(nums, x)}")