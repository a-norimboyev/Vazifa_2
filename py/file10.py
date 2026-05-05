"""
7-amaliy topshiriq, 10-mavzu:
Mantiqiy cheklovlar (Constraint Programming)

Vazifa:
A + B = 10 va A > 5 shartlarini qanoatlantiruvchi
barcha A va B qiymatlarini topish.
"""

solutions = [
    (A, B)
    for A in range(0, 11)
    for B in range(0, 11)
    if A + B == 10 and A > 5
]

print("Yechimlar (A, B):")
print(solutions)
