"""15-vazifa: Segmentlarni qoplash (greedy) — minimal nuqtalar soni.

Berilgan segmentlar to'plamida har bir segmentda kamida bitta nuqta
bo'ladigan eng kam nuqta sonini tanlash.
"""


def min_points_to_cover(segments):
    """Har bir segmentni kamida bitta nuqta bilan qoplaydigan
    minimal nuqtalar to'plamini qaytaradi."""
    segments_sorted = sorted(segments, key=lambda s: s[1])
    points = []

    for left, right in segments_sorted:
        if not points or points[-1] < left:
            points.append(right)

    return points


if __name__ == "__main__":
    test_segments = [
        [(1, 3), (2, 5), (3, 6)],
        [(4, 7), (1, 3), (2, 5), (5, 6)],
        [(0, 2), (3, 5), (7, 10), (1, 4), (6, 8)],
    ]

    for segments in test_segments:
        result = min_points_to_cover(segments)
        print(f"Segmentlar: {segments}")
        print(f"  Tanlangan nuqtalar: {result}")
        print(f"  Minimal nuqtalar soni: {len(result)}")
        print()
