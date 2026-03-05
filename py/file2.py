def sum_digits_iterative(n):
    total = 0
    n = abs(n)  # Manfiy sonlar bilan ham ishlash uchun
    while n > 0:
        total += n % 10  # Oxirgi raqamni qo'shish
        n //= 10         # Oxirgi raqamni olib tashlash
    return total

# Rekursiv usul
"""
def sum_digits_recursive(n):
    n = abs(n)
    # To'xtash sharti (Base case)
    if n == 0:
        return 0
    # Rekursiv qadam
    return (n % 10) + sum_digits_recursive(n // 10)
"""