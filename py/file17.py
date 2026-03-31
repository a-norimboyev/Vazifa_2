"""17-vazifa: Minimal platformalar soni (greedy).

Poyezdlarning kelish va ketish vaqtlari berilgan holatda
barcha poyezdlarni qabul qilish uchun zarur platformalar soni.
"""


def min_platforms(arrivals, departures):
    """Zarur bo'lgan eng kam platformalar sonini qaytaradi."""
    events = []
    for t in arrivals:
        events.append((t, 1))    # kelish
    for t in departures:
        events.append((t, -1))   # ketish

    events.sort(key=lambda e: (e[0], e[1]))

    current_platforms = 0
    max_platforms = 0

    for _, event_type in events:
        current_platforms += event_type
        if current_platforms > max_platforms:
            max_platforms = current_platforms

    return max_platforms


if __name__ == "__main__":
    arrivals   = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]

    print("Kelish vaqtlari: ", arrivals)
    print("Ketish vaqtlari: ", departures)
    result = min_platforms(arrivals, departures)
    print(f"Zarur platformalar soni: {result}")

    print()
    arrivals2   = [200, 210, 300, 320, 350, 500]
    departures2 = [230, 340, 320, 430, 400, 520]
    print("Kelish vaqtlari: ", arrivals2)
    print("Ketish vaqtlari: ", departures2)
    print(f"Zarur platformalar soni: {min_platforms(arrivals2, departures2)}")
