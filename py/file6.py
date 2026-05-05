"""
7-amaliy topshiriq, 6-mavzu:
Rekursiv mantiq (Fibonacci)

Vazifa:
Fibonacci qiymatini rekursiya bilan hisoblash.
Sikl ishlatilmaydi, formula to'g'ridan-to'g'ri aks etadi.
"""


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n manfiy bo'lmasligi kerak")
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("n ni kiriting: ").strip())
print(f"f({n}) = {fibonacci(n)}")
