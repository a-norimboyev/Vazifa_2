"""16-vazifa: Kutish vaqtini minimallashtirish (greedy).

n ta vazifa ijro vaqtlari berilgan. Umumiy kutish vaqtini
minimallashtiradigan tartibni aniqlash (SPT — Shortest Processing Time).
"""


def minimize_waiting_time(processing_times):
    """Optimal tartib va umumiy kutish vaqtini qaytaradi."""
    indexed_tasks = list(enumerate(processing_times))
    indexed_tasks.sort(key=lambda x: x[1])

    order = []
    total_wait = 0
    current_wait = 0

    for original_index, p_time in indexed_tasks:
        total_wait += current_wait
        order.append((original_index, p_time, current_wait))
        current_wait += p_time

    return order, total_wait


if __name__ == "__main__":
    tasks = [5, 2, 8, 1, 4]
    print(f"Vazifalarning ijro vaqtlari: {tasks}")

    order, total_wait = minimize_waiting_time(tasks)

    print("\nOptimal ijro tartibi:")
    print(f"{'Vazifa':<10} {'Ijro vaqti':<15} {'Kutish vaqti':<15}")
    print("-" * 40)
    for idx, p_time, wait in order:
        print(f"T{idx + 1:<9} {p_time:<15} {wait:<15}")

    print(f"\nUmumiy kutish vaqti: {total_wait}")
    avg_wait = total_wait / len(tasks)
    print(f"O'rtacha kutish vaqti: {avg_wait:.2f}")
