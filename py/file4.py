"""4-vazifa: tanlov saralash va har iteratsiyadan keyin chop etish."""


def selection_sort_with_steps(arr):
    result = arr[:]
    n = len(result)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j

        result[i], result[min_index] = result[min_index], result[i]
        print(f"{i + 1}-iteratsiya: {result}")

    return result


if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print("Boshlang'ich massiv:", data)
    final_arr = selection_sort_with_steps(data)
    print("Yakuniy massiv:", final_arr)