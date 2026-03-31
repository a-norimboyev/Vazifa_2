"""5-vazifa: qo'shish saralash (kamayish tartibida)."""


def insertion_sort_desc(arr):
    result = arr[:]

    for i in range(1, len(result)):
        key = result[i]
        j = i - 1

        while j >= 0 and result[j] < key:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = key

    return result


if __name__ == "__main__":
    nums = [5, 2, 9, 1, 5, 6]
    print("Boshlang'ich massiv:", nums)
    print("Kamayish bo'yicha saralangan:", insertion_sort_desc(nums))