"""3-vazifa: obyektlar massivini pufakchali saralash."""


def bubble_sort_objects(items, field, ascending=True):
    """Obyektlar ro'yxatini tanlangan maydon bo'yicha saralaydi."""
    result = items[:]
    n = len(result)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            left = result[j][field]
            right = result[j + 1][field]
            should_swap = left > right if ascending else left < right
            if should_swap:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break

    return result


if __name__ == "__main__":
    students = [
        {"ism": "Ali", "yosh": 20, "gpa": 3.2},
        {"ism": "Vali", "yosh": 19, "gpa": 3.8},
        {"ism": "Sardor", "yosh": 21, "gpa": 3.5},
    ]

    print("GPA bo'yicha saralash:")
    for student in bubble_sort_objects(students, "gpa"):
        print(student)