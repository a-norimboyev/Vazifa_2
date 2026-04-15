"""10-vazifa: Rekursiya tushunchasi va uning turlari."""


# ============================================================
# 1. TO'G'RIDAN-TO'G'RI REKURSIYA (Direct Recursion)
# Funksiya o'zini o'zi chaqiradi
# ============================================================
def sanash(n):
    """n dan 1 gacha sanaydi (to'g'ridan-to'g'ri rekursiya)."""
    if n <= 0:
        return
    print(n, end=" ")
    sanash(n - 1)


# ============================================================
# 2. BILVOSITA REKURSIYA (Indirect/Mutual Recursion)
# A funksiya B ni, B funksiya A ni chaqiradi
# ============================================================
def juft_mi(n):
    """Son juft ekanligini bilvosita rekursiya bilan tekshiradi."""
    if n == 0:
        return True
    return toq_mi(n - 1)


def toq_mi(n):
    """Son toq ekanligini bilvosita rekursiya bilan tekshiradi."""
    if n == 0:
        return False
    return juft_mi(n - 1)


# ============================================================
# 3. QUYRUQLI REKURSIYA (Tail Recursion)
# Rekursiv chaqiruv funksiyaning oxirgi amali
# ============================================================
def yigindi_quyruqli(n, jamlanma=0):
    """1 dan n gacha yig'indini quyruqli rekursiya bilan hisoblaydi."""
    if n <= 0:
        return jamlanma
    return yigindi_quyruqli(n - 1, jamlanma + n)


# ============================================================
# 4. DARAXTSIMON REKURSIYA (Tree Recursion)
# Funksiya o'zini bir necha marta chaqiradi
# ============================================================
def fibonachchi_daraxt(n):
    """Fibonachchi soni (daraxtsimon rekursiya — 2 ta chaqiruv)."""
    if n <= 1:
        return n
    return fibonachchi_daraxt(n - 1) + fibonachchi_daraxt(n - 2)


# ============================================================
# 5. ICHKI REKURSIYA (Nested Recursion)
# Rekursiv chaqiruv argument sifatida rekursiv chaqiruv oladi
# ============================================================
def ichki_rekursiya(n):
    """Ichki rekursiya namunasi."""
    if n > 100:
        return n - 10
    return ichki_rekursiya(ichki_rekursiya(n + 11))


if __name__ == "__main__":
    print("=" * 55)
    print("REKURSIYA TURLARI")
    print("=" * 55)

    # 1. To'g'ridan-to'g'ri
    print("\n1. To'g'ridan-to'g'ri rekursiya (5 dan 1 gacha):")
    sanash(5)
    print()

    # 2. Bilvosita
    print("\n2. Bilvosita rekursiya (juft/toq tekshirish):")
    for son in range(8):
        print(f"  {son}: juft={juft_mi(son)}, toq={toq_mi(son)}")

    # 3. Quyruqli
    print("\n3. Quyruqli rekursiya (1 dan n gacha yig'indi):")
    for n in [5, 10, 100]:
        print(f"  yig'indi(1..{n}) = {yigindi_quyruqli(n)}")

    # 4. Daraxtsimon
    print("\n4. Daraxtsimon rekursiya (Fibonachchi):")
    for i in range(10):
        print(f"  F({i}) = {fibonachchi_daraxt(i)}")

    # 5. Ichki
    print("\n5. Ichki rekursiya (McCarthy 91 funksiyasi):")
    for n in [85, 95, 100, 105, 110]:
        print(f"  f({n}) = {ichki_rekursiya(n)}")
