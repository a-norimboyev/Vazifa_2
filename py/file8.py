"""
7-amaliy topshiriq, 8-mavzu:
Ma'lumotlarni saralash (Sorting)

Vazifa:
O'quvchilarni avval baho bo'yicha kamayish tartibida,
so'ng ism bo'yicha alifbo tartibida saralash.
"""

students = [
    {"name": "Ali", "grade": 86},
    {"name": "Zarina", "grade": 91},
    {"name": "Bekzod", "grade": 91},
    {"name": "Madina", "grade": 78},
    {"name": "Anvar", "grade": 86},
]

sorted_students = sorted(students, key=lambda s: (-s["grade"], s["name"]))

print("Saralangan ro'yxat:")
print(sorted_students)
