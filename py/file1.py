"""1-vazifa: satrlar massivida chiziqli qidiruv."""


def linear_search_first(strings, target):
    """Berilgan satrning birinchi uchrashgan indeksini qaytaradi."""
    for index, value in enumerate(strings):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    words = ["olma", "anor", "nok", "anor", "shaftoli"]
    query = "anor"
    result = linear_search_first(words, query)
    print(f"Massiv: {words}")
    print(f"Qidirilgan satr: {query}")
    print(f"Birinchi indeks: {result}")