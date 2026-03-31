"""12-vazifa: Bo'linish va zabt etish usuli bilan eng ko'p uchraydigan elementni topish.

Masalaning sharti: n/2 martadan ko'p uchraydigan elementni topish.
Boyer-Moore voting + divide & conquer yechimi.
"""


def majority_element_dc(arr, left=None, right=None):
    """Bo'lin va zabt et usuli bilan majority element topish."""
    if left is None:
        left = 0
        right = len(arr) - 1

    if left == right:
        return arr[left]

    mid = (left + right) // 2
    left_majority = majority_element_dc(arr, left, mid)
    right_majority = majority_element_dc(arr, mid + 1, right)

    if left_majority == right_majority:
        return left_majority

    left_count = sum(1 for i in range(left, right + 1) if arr[i] == left_majority)
    right_count = sum(1 for i in range(left, right + 1) if arr[i] == right_majority)

    if left_count > (right - left + 1) // 2:
        return left_majority
    if right_count > (right - left + 1) // 2:
        return right_majority

    return None


if __name__ == "__main__":
    test_cases = [
        [3, 3, 4, 2, 3, 3, 3],
        [1, 2, 3, 4, 5],
        [7, 7, 7, 2, 7, 1, 7],
    ]
    for arr in test_cases:
        result = majority_element_dc(arr)
        if result is not None:
            print(f"Massiv: {arr}  ->  Ko'pchilik element: {result}")
        else:
            print(f"Massiv: {arr}  ->  Ko'pchilik element topilmadi")
