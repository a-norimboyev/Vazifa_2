"""12-vazifa: Rekursiv algoritmlarni dasturlash tilida amalga oshirish."""

import sys

# Rekursiya chegarasini oshirish (chuqur rekursiya uchun)
sys.setrecursionlimit(5000)


# ============================================================
# 1. QUVVATGA OSHIRISH (Power) — rekursiv
# ============================================================
def quvvat(asos, daraja):
    """a^n ni rekursiv hisoblaydi (tez quvvatlash)."""
    if daraja == 0:
        return 1
    if daraja < 0:
        return 1 / quvvat(asos, -daraja)
    if daraja % 2 == 0:
        yarim = quvvat(asos, daraja // 2)
        return yarim * yarim
    return asos * quvvat(asos, daraja - 1)


# ============================================================
# 2. EKUB (GCD) — Evklid algoritmiy
# ============================================================
def ekub(a, b):
    """Eng katta umumiy bo'luvchi (Evklid algoritmi)."""
    if b == 0:
        return a
    return ekub(b, a % b)


# ============================================================
# 3. IKKILIK QIDIRISH (Binary Search) — rekursiv
# ============================================================
def ikkilik_qidirish(massiv, qiymat, chap=0, ong=None):
    """Saralangan massivda ikkilik qidirish."""
    if ong is None:
        ong = len(massiv) - 1
    if chap > ong:
        return -1
    orta = (chap + ong) // 2
    if massiv[orta] == qiymat:
        return orta
    elif massiv[orta] < qiymat:
        return ikkilik_qidirish(massiv, qiymat, orta + 1, ong)
    else:
        return ikkilik_qidirish(massiv, qiymat, chap, orta - 1)


# ============================================================
# 4. SATRNI TESKARI QILISH — rekursiv
# ============================================================
def teskari_satr(s):
    """Satrni rekursiv teskari qiladi."""
    if len(s) <= 1:
        return s
    return teskari_satr(s[1:]) + s[0]


# ============================================================
# 5. PALINDROM TEKSHIRISH — rekursiv
# ============================================================
def palindrom_mi(s):
    """Satr palindrom ekanligini rekursiv tekshiradi."""
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom_mi(s[1:-1])


# ============================================================
# 6. SON RAQAMLARINING YIG'INDISI — rekursiv
# ============================================================
def raqamlar_yigindisi(n):
    """Sonning raqamlari yig'indisini hisoblaydi."""
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + raqamlar_yigindisi(n // 10)


# ============================================================
# 7. MASSIVDAGI ENG KATTA ELEMENT — rekursiv
# ============================================================
def eng_katta(massiv, n=None):
    """Massivdagi eng katta elementni rekursiv topadi."""
    if n is None:
        n = len(massiv)
    if n == 1:
        return massiv[0]
    return max(massiv[n - 1], eng_katta(massiv, n - 1))


if __name__ == "__main__":
    print("=" * 55)
    print("REKURSIV ALGORITMLAR AMALGA OSHIRILISHI")
    print("=" * 55)

    # 1. Quvvatga oshirish
    print("\n1. QUVVATGA OSHIRISH:")
    testlar = [(2, 10), (3, 5), (5, 0), (2, -3)]
    for asos, daraja in testlar:
        print(f"   {asos}^{daraja} = {quvvat(asos, daraja)}")

    # 2. EKUB
    print("\n2. EKUB (Evklid):")
    juftlar = [(48, 18), (100, 75), (17, 13)]
    for a, b in juftlar:
        print(f"   EKUB({a}, {b}) = {ekub(a, b)}")

    # 3. Ikkilik qidirish
    print("\n3. IKKILIK QIDIRISH:")
    massiv = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    for qiymat in [23, 72, 50]:
        natija = ikkilik_qidirish(massiv, qiymat)
        print(f"   {qiymat} → indeks: {natija}")

    # 4. Satrni teskari qilish
    print("\n4. SATRNI TESKARI QILISH:")
    for satr in ["salom", "python", "rekursiya"]:
        print(f"   '{satr}' → '{teskari_satr(satr)}'")

    # 5. Palindrom tekshirish
    print("\n5. PALINDROM TEKSHIRISH:")
    for satr in ["madam", "racecar", "salom", "abacaba"]:
        print(f"   '{satr}' → {palindrom_mi(satr)}")

    # 6. Raqamlar yig'indisi
    print("\n6. RAQAMLAR YIG'INDISI:")
    for son in [123, 9999, 5040, 11111]:
        print(f"   {son} → {raqamlar_yigindisi(son)}")

    # 7. Eng katta element
    print("\n7. ENG KATTA ELEMENT:")
    massiv = [34, 7, 89, 12, 56, 3, 91, 45]
    print(f"   {massiv} → max = {eng_katta(massiv)}")
