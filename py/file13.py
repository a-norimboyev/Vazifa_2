"""13-vazifa: Rekursiv va iterativ analoglarni solishtirish (natija va samaradorlik)."""

import time
import sys

sys.setrecursionlimit(10000)


# ============================================================
# 1. FAKTORIAL — rekursiv vs iterativ
# ============================================================
def faktorial_rekursiv(n):
    if n <= 1:
        return 1
    return n * faktorial_rekursiv(n - 1)


def faktorial_iterativ(n):
    natija = 1
    for i in range(2, n + 1):
        natija *= i
    return natija


# ============================================================
# 2. FIBONACHCHI — rekursiv vs iterativ
# ============================================================
def fib_rekursiv(n):
    """Oddiy rekursiv (sekin — eksponensial)."""
    if n <= 1:
        return n
    return fib_rekursiv(n - 1) + fib_rekursiv(n - 2)


def fib_memo(n, xotira={}):
    """Memoizatsiyali rekursiv (tez)."""
    if n in xotira:
        return xotira[n]
    if n <= 1:
        return n
    xotira[n] = fib_memo(n - 1, xotira) + fib_memo(n - 2, xotira)
    return xotira[n]


def fib_iterativ(n):
    """Iterativ (eng tez)."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ============================================================
# 3. YIG'INDI (1..n) — rekursiv vs iterativ
# ============================================================
def yigindi_rekursiv(n):
    if n <= 0:
        return 0
    return n + yigindi_rekursiv(n - 1)


def yigindi_iterativ(n):
    return sum(range(1, n + 1))


def yigindi_formula(n):
    return n * (n + 1) // 2


# ============================================================
# VAQTNI O'LCHASH YORDAMCHI FUNKSIYASI
# ============================================================
def vaqt_olcha(funksiya, *args, takrorlar=100):
    """Funksiya bajarilish vaqtini o'lchaydi."""
    boshi = time.perf_counter()
    for _ in range(takrorlar):
        natija = funksiya(*args)
    vaqt = (time.perf_counter() - boshi) / takrorlar
    return natija, vaqt


if __name__ == "__main__":
    print("=" * 65)
    print("REKURSIV vs ITERATIV SOLISHTIRISH")
    print("=" * 65)

    # 1. Faktorial solishtirish
    print("\n1. FAKTORIAL SOLISHTIRISH:")
    print(f"   {'n':>6} | {'Rekursiv (s)':>14} | {'Iterativ (s)':>14} | {'Tezlik farqi':>13}")
    print("   " + "-" * 55)
    for n in [10, 100, 500, 1000]:
        _, rek_vaqt = vaqt_olcha(faktorial_rekursiv, n)
        natija, iter_vaqt = vaqt_olcha(faktorial_iterativ, n)
        farq = rek_vaqt / iter_vaqt if iter_vaqt > 0 else 0
        print(f"   {n:>6} | {rek_vaqt:>14.8f} | {iter_vaqt:>14.8f} | {farq:>12.1f}x")

    # 2. Fibonachchi solishtirish
    print("\n2. FIBONACHCHI SOLISHTIRISH:")
    print(f"   {'n':>4} | {'Oddiy rek. (s)':>15} | {'Memo rek. (s)':>14} | {'Iterativ (s)':>13}")
    print("   " + "-" * 55)
    for n in [10, 20, 30]:
        _, rek_vaqt = vaqt_olcha(fib_rekursiv, n, takrorlar=10)
        _, memo_vaqt = vaqt_olcha(fib_memo, n, takrorlar=1000)
        _, iter_vaqt = vaqt_olcha(fib_iterativ, n, takrorlar=1000)
        print(f"   {n:>4} | {rek_vaqt:>15.8f} | {memo_vaqt:>14.8f} | {iter_vaqt:>13.8f}")

    # Natijalar to'g'riligini tekshirish
    print(f"\n   F(30): rekursiv={fib_rekursiv(30)}, memo={fib_memo(30)}, iterativ={fib_iterativ(30)}")

    # 3. Yig'indi solishtirish
    print("\n3. YIG'INDI (1..n) SOLISHTIRISH:")
    print(f"   {'n':>6} | {'Rekursiv (s)':>14} | {'Iterativ (s)':>14} | {'Formula (s)':>13}")
    print("   " + "-" * 55)
    for n in [100, 500, 1000, 3000]:
        _, rek_vaqt = vaqt_olcha(yigindi_rekursiv, n)
        _, iter_vaqt = vaqt_olcha(yigindi_iterativ, n)
        natija, form_vaqt = vaqt_olcha(yigindi_formula, n)
        print(f"   {n:>6} | {rek_vaqt:>14.8f} | {iter_vaqt:>14.8f} | {form_vaqt:>13.8f}")

    # Xulosa
    print("\n" + "=" * 65)
    print("XULOSA:")
    print("=" * 65)
    print("  - Rekursiya kodi sodda va tushunarli, lekin sekinroq.")
    print("  - Iterativ usul tezroq va kamroq xotira ishlatadi.")
    print("  - Memoizatsiya rekursiyani tezlashtiradi (Fibonachchi uchun).")
    print("  - Katta n uchun rekursiya stack overflow xatosiga olib kelishi mumkin.")
    print("  - Formula mavjud bo'lsa, eng tez usul — matematika!")
