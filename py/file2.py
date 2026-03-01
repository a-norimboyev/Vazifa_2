"""
VAZIFA 2: Sonning raqamlari yig'indisini hisoblash - ITERATIV vs REKURSIV

MISOL: 12345 sonining raqamlari yig'indisi = 1+2+3+4+5 = 15
"""

import time

print("=" * 70)
print("VAZIFA 2: RAQAMLARI YIG'INDISINI HISOBLASH - ITERATIV vs REKURSIV")
print("=" * 70)

# ============================================================================
# 1. ITERATIV (TAKRORLANUVCHI) USUL
# ============================================================================
print("\n1. ITERATIV USUL")
print("-" * 70)

def sum_of_digits_iterative(n):
    """
    PSEVDOKOD:
    ┌────────────────────────────────────┐
    │ ALGORITM: Sum_Digits_Iterative(n)  │
    │ INPUT: n - butun son               │
    │ OUTPUT: sum - raqamlari yig'indisi │
    │                                    │
    │ 1. n ← |n| (absolyut qiymat)       │
    │ 2. sum ← 0                         │
    │ 3. WHILE n > 0 DO                  │
    │ 4.    digit ← n mod 10             │
    │ 5.    sum ← sum + digit            │
    │ 6.    n ← n div 10                 │
    │ 7. END WHILE                       │
    │ 8. RETURN sum                      │
    └────────────────────────────────────┘
    """
    n = abs(n)  # Manfiy sonlarni ijobiyga o'tkazish
    total = 0
    
    while n > 0:
        digit = n % 10        # Oxirgi raqamni olish
        total += digit        # Yig'indiga qo'shish
        n = n // 10           # Oxirgi raqamni o'chirish
    
    return total

# ITERATIV USUL TRASSIROVKASI
print("\nMISCHON: 12345")
number = 12345
print(f"Kiritilgan son: {number}")
print("\nQadamma-qadam ishlash:")

n = number
total = 0
step = 1

while n > 0:
    digit = n % 10
    total += digit
    print(f"Qadam {step}: digit={digit}, n={n}, yig'indi={total}")
    n = n // 10
    step += 1

print(f"\nIterativ usul natijasi: {sum_of_digits_iterative(number)}")

# ============================================================================
# 2. REKURSIV (O'Z-O'ZIGA CHAQIRUVCHAN) USUL
# ============================================================================
print("\n" + "=" * 70)
print("2. REKURSIV USUL")
print("-" * 70)

def sum_of_digits_recursive(n):
    """
    PSEVDOKOD:
    ┌────────────────────────────────────┐
    │ ALGORITM: Sum_Digits_Recursive(n)  │
    │ INPUT: n - butun son               │
    │ OUTPUT: raqamlari yig'indisi       │
    │                                    │
    │ 1. IF n == 0 THEN                  │
    │ 2.    RETURN 0  (asosiy case)      │
    │ 3. ELSE                            │
    │ 4.    RETURN (n mod 10) +          │
    │          Sum_Digits_Recursive(     │
    │              n div 10)             │
    │ 5. END IF                          │
    └────────────────────────────────────┘
    """
    n = abs(n)
    
    # Asosiy sharty
    if n == 0:
        return 0
    
    # Rekursiv chaqiruv
    return (n % 10) + sum_of_digits_recursive(n // 10)

# REKURSIV USUL TRASSIROVKASI
print("\nMISOLON: 12345")
print("Rekursiv chaqiruvlar tartibi:\n")

call_count = [0]  # Chaqiruvlar sonini hisoblash

def sum_of_digits_recursive_trace(n, depth=0):
    call_count[0] += 1
    indent = "  " * depth
    n_abs = abs(n) if depth == 0 else n
    
    print(f"{indent}Chaqiruv {call_count[0]}: sum_of_digits({n})")
    
    if n == 0:
        print(f"{indent}  → Asosiy sharty: return 0")
        return 0
    
    digit = n % 10
    result = digit + sum_of_digits_recursive_trace(n // 10, depth + 1)
    print(f"{indent}  → return {digit} + {result - digit} = {result}")
    return result

result_trace = sum_of_digits_recursive_trace(number)
print(f"\nRekursiv usul natijasi: {sum_of_digits_recursive(number)}")

# ============================================================================
# 3. SAMARADORLIK TAQQOSLASH
# ============================================================================
print("\n" + "=" * 70)
print("3. SAMARADORLIK TAQQOSLASH")
print("-" * 70)

test_numbers = [123, 9876, 123456, 9876543, 123456789]

print(f"{'Son':<15} {'Iterativ (ms)':<15} {'Rekursiv (ms)':<15} {'Nisbat':<10}")
print("-" * 55)

for num in test_numbers:
    # Iterativ
    start = time.perf_counter()
    for _ in range(100000):
        sum_of_digits_iterative(num)
    iterative_time = (time.perf_counter() - start) * 1000
    
    # Rekursiv
    start = time.perf_counter()
    for _ in range(100000):
        sum_of_digits_recursive(num)
    recursive_time = (time.perf_counter() - start) * 1000
    
    ratio = recursive_time / iterative_time
    print(f"{num:<15} {iterative_time:<15.4f} {recursive_time:<15.4f} {ratio:.2f}x")

# ============================================================================
# 4. XULOSA
# ============================================================================
print("\n" + "=" * 70)
print("4. TAQQOSLAN VA XULOSA")
print("=" * 70)

print("""
ITERATIV USUL:
✓ Tezroq (Stack memory ishlatmaydi)
✓ Stack overflow xavfi yo'q
✓ Katta sonlar bilan ishlaydi
⚠ Kodda loop kerak

REKURSIV USUL:
✓ Kod tushunarli va qisqaroq
✓ Matematik tasviri aniq
⚠ Sekinroq (funksiya chaqiruv overhead)
⚠ Chuqur rekursiya → Stack overflow xavfi

NATIJA: ITERATIV USUL YAXSHIROQ!
Sabab: Iterativ usul tezroq va xavfsizroq.
       Production kodida iterativ usuldan foydalanish tavsiya etiladi.
""")

print("\nNATIJA TEKSHIRISH:")
print(f"Iterativ:  {sum_of_digits_iterative(12345)}")
print(f"Rekursiv:  {sum_of_digits_recursive(12345)}")
print(f"Mos keladi: {sum_of_digits_iterative(12345) == sum_of_digits_recursive(12345)}")

