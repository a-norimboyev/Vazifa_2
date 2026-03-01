"""
VAZIFA 3: TUB SONNI TEKSHIRISH - SODDA vs OPTIMALLASHTIRILGAN USUL
"""

import math
import time

print("=" * 70)
print("VAZIFA 3: TUB SONNI TEKSHIRISH ALGORITMINI OPTIMALLASHTIRISH")
print("=" * 70)

# ============================================================================
# 1. SODDA (NAIV) USUL - 2 dan n-1 gacha tekshirish
# ============================================================================
print("\n1. SODDA (NAIV) USUL")
print("-" * 70)

def is_prime_naive(n):
    """
    PSEVDOKOD:
    ┌───────────────────────────────────┐
    │ ALGORITM: IsP rime_Naive(n)        │
    │ INPUT: n - tekshiriladigan son    │
    │ OUTPUT: true/false                │
    │                                   │
    │ 1. IF n < 2 THEN                  │
    │ 2.    RETURN false                │
    │ 3. END IF                         │
    │ 4. i ← 2                          │
    │ 5. WHILE i < n DO                 │
    │ 6.    IF n mod i == 0 THEN        │
    │ 7.       RETURN false             │
    │ 8.    END IF                      │
    │ 9.    i ← i + 1                   │
    │ 10. END WHILE                     │
    │ 11. RETURN true                   │
    └───────────────────────────────────┘
    
    VAQT MURAKKABLIGI: O(n) - juda sekin!
    """
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

# Sodda usul misoli
print("\nMISAL: 17 soni tub mi?")
print("\nTekshirish: 2 dan 16 gacha:")

n = 17
print(f"17 % 2 = {17 % 2} (0 emas) ✓")
print(f"17 % 3 = {17 % 3} (0 emas) ✓")
print(f"17 % 4 = {17 % 4} (0 emas) ✓")
print(f"... (barchasi 0 emas)")
print(f"17 % 16 = {17 % 16} (0 emas) ✓")
print(f"\nNATIJA: 17 - TUB SON ✓")
print(f"Funksiya: {is_prime_naive(17)}")

# ============================================================================
# 2. OPTIMALLASHTIRILGAN USUL
# ============================================================================
print("\n" + "=" * 70)
print("2. OPTIMALLASHTIRILGAN USUL")
print("-" * 70)

def is_prime_optimized(n):
    """
    OPTIMALASHTIRISHLAR:
    1. Faqat √n gacha tekshirish (matematikasi: n = a×b bo'lsa, 
       min(a,b) <= √n)
    2. Faqat toq bo'luvchilarni tekshirish (2 ga bo'lingan ketma-ket tekshir)
    
    PSEVDOKOD:
    ┌────────────────────────────────────┐
    │ ALGORITM: IsPrime_Optimized(n)     │
    │ INPUT: n - tekshiriladigan son    │
    │ OUTPUT: true/false                │
    │                                   │
    │ 1. IF n < 2 THEN                  │
    │ 2.    RETURN false                │
    │ 3. END IF                         │
    │ 4. IF n == 2 THEN                 │
    │ 5.    RETURN true                 │
    │ 6. END IF                         │
    │ 7. IF n mod 2 == 0 THEN           │
    │ 8.    RETURN false                │
    │ 9. END IF                         │
    │ 10.i ← 3                          │
    │ 11.WHILE i <= √n DO               │
    │ 12.   IF n mod i == 0 THEN        │
    │ 13.      RETURN false             │
    │ 14.   END IF                      │
    │ 15.   i ← i + 2  (faqat toq)      │
    │ 16.END WHILE                      │
    │ 17.RETURN true                    │
    └────────────────────────────────────┘
    
    VAQT MURAKKABLIGI: O(√n) - ancha tezroq!
    """
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    # Faqat √n gacha va faqat toq bo'luvchilarni tekshirish
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True

# Optimallashtirilgan usul misoli
print("\nMISAL: 17 soni tub mi? (OPTIMALLASHTIRILGAN)")
print(f"\n√17 ≈ {math.sqrt(17):.2f}")
print(f"Tekshirish: 2 dan {int(math.sqrt(17))} gacha faqat toq raqamlar:")

n = 17
print(f"17 % 2 = {17 % 2} (juft emas) ✓")
print(f"17 % 3 = {17 % 3} (0 emas) ✓")
print(f"√17 gacha yetib boshladik, boshqa tekshirish kerak emas!")
print(f"\nNATIJA: 17 - TUB SON ✓")
print(f"Funksiya: {is_prime_optimized(17)}")

# ============================================================================
# 3. ISHLASH TEZLIGINI TAQQOSLASH
# ============================================================================
print("\n" + "=" * 70)
print("3. ISHLASH TEZLIGINI TAQQOSLASH")
print("-" * 70)

test_numbers = [97, 541, 2027, 9973, 99991]

print(f"{'Son':<12} {'Sodda (ms)':<15} {'Optimallash(ms)':<15} {'Tezlik':<10}")
print("-" * 55)

for num in test_numbers:
    # Sodda usul
    start = time.perf_counter()
    for _ in range(10000):
        is_prime_naive(num)
    naive_time = (time.perf_counter() - start) * 1000
    
    # Optimallashtirilgan
    start = time.perf_counter()
    for _ in range(10000):
        is_prime_optimized(num)
    optimized_time = (time.perf_counter() - start) * 1000
    
    speedup = naive_time / optimized_time
    print(f"{num:<12} {naive_time:<15.4f} {optimized_time:<15.4f} {speedup:.1f}x")

# ============================================================================
# 4. MATRITSA ANALIZI
# ============================================================================
print("\n" + "=" * 70)
print("4. MUAMMOLI SONLAR BILAN TEKSHIRISH")
print("=" * 70)

print("\nTub sonlar:")
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
for p in primes:
    naive_result = is_prime_naive(p)
    optimized_result = is_prime_optimized(p)
    match = "✓" if naive_result == optimized_result else "✗"
    print(f"{p:3d}: Sodda={naive_result}, Optimallash={optimized_result} {match}")

print("\nTub bo'lmagan sonlar:")
composites = [4, 6, 8, 9, 10, 12, 15, 20, 21, 25]
for c in composites:
    naive_result = is_prime_naive(c)
    optimized_result = is_prime_optimized(c)
    match = "✓" if naive_result == optimized_result else "✗"
    print(f"{c:3d}: Sodda={naive_result}, Optimallash={optimized_result} {match}")

# ============================================================================
# 5. XULOSA
# ============================================================================
print("\n" + "=" * 70)
print("5. XULOSA VA TAVSIYALAR")
print("=" * 70)

print("""
SODDA USUL (Naive):
⚠ VAQT MURAKKABLIGI: O(n)
⚠ 100 sonni tekshirish: ~98 ta bo'linish
⚠ 1000 sonni tekshirish: ~998 ta bo'linish
⚠ Katta sonlar uchun juda sekin

OPTIMALLASHTIRILGAN USUL:
✓ VAQT MURAKKABLIGI: O(√n)
✓ 100 sonni tekshirish: ~10 ta bo'linish
✓ 1000 sonni tekshirish: ~31 ta bo'linish
✓ 10x - 30x tezroq!

OPTIMALASHTIRISHNING ACHANILIGI:
1. √n gacha tekshirish: Agar n = a×b va a > √n, b < √n bo'lsa, 
   b allaqachon tekshirilgan bo'ladi
2. Faqat toq raqamlar: 2 dan oldin barcha juft sonlar tekshirish mumkin

NATIJA: OPTIMALLASHTIRILGAN USUL KATTA SONLAR UCHUN ISHLIQ PRAKTIKADA 
        YAGONA QABUL QILINADIGAN USULDIR!

Real misollar:
- Kriptografiya: Katta tub sonlar tekshirish kerak (1024+ bit)
- Hashing: Hash jadvallari uchun tub sonlar kerak
- Algoritm tuzish: Tub sonlarni topish uchun Sieve of Eratosthenes tavsiya etiladi
""")

