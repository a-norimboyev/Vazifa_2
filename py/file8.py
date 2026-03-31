"""8-vazifa: saralangan massivda qo'shish pozitsiyasi (ikkilik qidiruv)."""


def find_insertion_position(arr, target):
    """Target joylashishi kerak bo'lgan eng chap indeksni qaytaradi."""
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    x = 4
    pos = find_insertion_position(nums, x)
    print("Massiv:", nums)
    print(f"{x} uchun qo'shish pozitsiyasi: {pos}")