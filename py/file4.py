"""
VAZIFA 4: SELECTION SORT - TANLASH USULI BILAN SARALASH ALGORITMINI ISHLAB CHIQING
"""

print("=" * 75)
print("VAZIFA 4: TANLASH USULI (SELECTION SORT) BILAN SARALASH")
print("=" * 75)

# ============================================================================
# 1. ALGORITMI TAVSIFI
# ============================================================================
print("\n1. ALGORITMI TAVSIFI")
print("-" * 75)

print("""
TANLASH USULI (Selection Sort) - Qanday ishlaydi:

1. Massivning birinchi elementidan boshlanadi
2. Qolgan barcha elementlardan eng kichik elementni topadi
3. Topilgan eng kichik elementni birinchi element bilan almashtiradi
4. Keyin ikkinchi elementdan boshlanadi va u'ng tarafidagilardan 
   eng kichikini topadi
5. Bu jarayon massivning oxirigacha davom etadi

NATIJA: Massiv kichikdan kattaga qarab saralanadi

VAQT MURAKKABLIGI: O(n²) - dosta sekin, lekin tushunarli
JOYNI ISHLATISH: O(1) - qo'shimcha joy kerak emas (In-place)
BARQARARLIGI: Qo'shimcha barkararlik kerak (Unstable)
""")

# ============================================================================
# 2. PSEVDOKOD
# ============================================================================
print("\n2. PSEVDOKOD")
print("-" * 75)

print("""
PSEVDOKOD:
┌─────────────────────────────────────────────────────┐
│ ALGORITM: SelectionSort(array)                      │
│ INPUT: array - tartiblandi keladigan massiv         │
│ OUTPUT: array - tartiblangan massiv                 │
│                                                     │
│ 1. FOR i ← 0 TO length(array)-2 DO                  │
│ 2.    min_index ← i                                 │
│ 3.    FOR j ← i+1 TO length(array)-1 DO             │
│ 4.       IF array[j] < array[min_index] THEN        │
│ 5.          min_index ← j                           │
│ 6.       END IF                                     │
│ 7.    END FOR                                       │
│ 8.    SWAP(array[i], array[min_index])              │
│ 9. END FOR                                          │
│ 10. RETURN array                                    │
└─────────────────────────────────────────────────────┘
""")

# ============================================================================
# 3. BLOK-SXEMA (MATNLI)
# ============================================================================
print("\n3. BLOK-SXEMA (MATNLI KO'RINISH)")
print("-" * 75)

print("""
                        ┌──────────────┐
                        │ START        │
                        └──────┬───────┘
                               │
                        ┌──────▼──────────┐
                        │ array qabul qil │
                        └──────┬──────────┘
                               │
                        ┌──────▼──────────────────┐
                        │ i = 0                   │
                        └──────┬──────────────────┘
                               │
                        ┌──────▼──────────────────┐
                        │ i < len(arr)-1? ║        TASHQARISI SIKL
                        └──┬───────────┬──────────┘
                    YOQIM│         │ HA
                           │         │
                 ┌─────────▼─┐   ┌──▼──────────────┐
                 │ i = i + 1 │   │ min_idx = i     │
                 └────┬──────┘   └──┬───────────────┘
                      │            │
                      │      ┌──────▼──────────────┐
                      │      │ j = i + 1           │
                      │      └──┬────────────────┬─┐ ICHKARISI SIKL
                      │         │              │
                      │         │    ┌─────────▼──────────┐
                      │         │    │ j < len(arr)? │ │
                      │  YOQIM  │    └──┬────────┬────────┘
                      │         │       │      │ HA
                      │         │       │    ┌─▼──────────────────┐
                      │         │       │    │ arr[j] <           │
                      │         │       │    │ arr[min_idx]?      │
                      │         │       │    └──┬─────────┬───────┘
                      │         │       │    HA │         │ YOQIM
                      │         │       │    ┌──▼─┐       │
                      │         │       │    │min │       │
                      │         │       │    │idx │       │
                      │         │       │    │= j │       │
                      │         │       │    └──┬─┘       │
                      │         │       │       │        │
                      │         │       └───────┼────────┘
                      │         │               │
                      │         │       ┌───────▼──┐
                      │         │       │ j = j+1  │
                      │         │       └─────┬────┘
                      │         │             │
                      │         └─────────────┘ (qayta ichkarisi sikl)
                      │
                      │      ┌──────────────────────────┐
                      │      │ SWAP(arr[i], arr[min_idx])
                      │      └──────────────────────────┘
                      │                 │
                      └─────────────────┘  (qayta tashqarisi sikl)
                               │
                        ┌──────▼──────────┐
                        │ RETURN array    │
                        └──────┬──────────┘
                               │
                        ┌──────▼──────────┐
                        │ END             │
                        └─────────────────┘
""")

# ============================================================================
# 4. PYTHON KODI
# ============================================================================
print("\n4. PYTHON KODI VA AMALGA OSHIRISH")
print("-" * 75)

def selection_sort(array):
    """
    Selection Sort algoritmi
    
    Args:
        array: Saralanishi kerak bo'lgan massiv
    
    Returns:
        Saralangan massiv
    """
    n = len(array)
    
    # Tashqarisi sikl - har bir pozitsiya uchun
    for i in range(n - 1):
        # Eng kichik elementning indeksini topish
        min_index = i
        
        # Ichkarisi sikl - qolgan elementlarni tekshirish
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        
        # Joylarni almashtirish (swap)
        array[i], array[min_index] = array[min_index], array[i]
    
    return array


# ============================================================================
# 5. MISOL ASOSIDA TRASSIROVKA
# ============================================================================
print("\nMISAL: [5, 2, 8, 1, 9] ni saralash\n")

array = [5, 2, 8, 1, 9]
print(f"Boshlang'ich: {array}\n")

n = len(array)

for i in range(n - 1):
    print(f"{'='*70}")
    print(f"QO'L I: i = {i}, Joriy element = {array[i]}")
    print(f"Joriyotda: {array}")
    print()
    
    min_index = i
    print(f"  {i+1}-qadam: {array[i:]} ichidan eng kichikni topish:")
    
    for j in range(i + 1, n):
        if array[j] < array[min_index]:
            old_min = min_index
            min_index = j
            print(f"    j={j}: array[{j}]={array[j]} < array[{old_min}]={array[old_min]} ✓ Min_index={min_index}")
        else:
            print(f"    j={j}: array[{j}]={array[j]} >= array[{min_index}]={array[min_index]} ✗")
    
    print(f"\n  {i+2}-qadam: Eng kichik element = array[{min_index}] = {array[min_index]}")
    print(f"  {i+3}-qadam: array[{i}] va array[{min_index}] ni almashtirish")
    
    if i != min_index:
        array[i], array[min_index] = array[min_index], array[i]
        print(f"  NATIJA: {array}")
    else:
        print(f"  (Allaqachon o'z joyida)")
    print()

print(f"{'='*70}")
print(f"YAKUNIY NATIJA: {array}")
print(f"{'='*70}\n")

# ============================================================================
# 6. FUNKSIYANI TESTLASH
# ============================================================================
print("\n6. FUNKSIYANI TURLI MASSIVLAR BILAN TESTLASH")
print("-" * 75)

test_cases = [
    ([64, 34, 25, 12, 22, 11, 90], "Tasodifiy"),
    ([5, 4, 3, 2, 1], "Teskari tartiblangan"),
    ([1, 2, 3, 4, 5], "Allaqachon saralangan"),
    ([5, 5, 5, 5], "Barcha o'xshash"),
    ([42], "Bitta element"),
    ([], "Bo'sh massiv"),
    ([9, 1, 8, 2, 7, 3], "Aralash"),
]

for test_array, description in test_cases:
    original = test_array.copy()
    result = selection_sort(test_array.copy())
    print(f"\n{description}:")
    print(f"  Oldingi: {original}")
    print(f"  Keyin:   {result}")
    print(f"  To'g'ri: {result == sorted(original)}")

# ============================================================================
# 7. MURAKKABLIK TAHLILI
# ============================================================================
print("\n" + "=" * 75)
print("7. MURAKKABLIK TAHLILI")
print("=" * 75)

print("""
VAQT MURAKKABLIGI:
├─ Eng yomon holat: O(n²) - agar massiv teskari tartiblangan bo'lsa
├─ O'rtacha holat:  O(n²) - har doim bir xil
└─ Eng yaxshi holat: O(n²) - hatto saralangan bo'lgan massiv uchun ham

JOYNI ISHLATISH: O(1) - qo'shimcha massiv kerak emas (in-place)

SARALASHNING BARQARARLIGI: Unstable
  Misol: [(5, 'a'), (2, 'b'), (5, 'c')]
  Agar 'a' va 'c' almashsa, tartib o'zgarib qoladi

TAVSIYALAR:
✗ Katta massivlar (n > 1000) uchun ishlatmang
✓ Kichik massivlar uchun yaxshi
✓ O'qitishga qulay - tushunarli
✓ Buyum almashning minimalli bo'lganida yaxshi (Merge Sort kattamas)
""")

# ============================================================================
# 8. OTHER SORTING ALGORITHMS BILAN TAQQOSLASH
# ============================================================================
print("\n" + "=" * 75)
print("8. ISHLASH TEZLIGINI TAQQOSLASH")
print("=" * 75)

import time
import random

sizes = [100, 500, 1000]
print(f"\n{'Hajm':<10} {'Selection Sort (ms)':<20}")
print("-" * 35)

def selection_sort_simple(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

for size in sizes:
    test_array = [random.randint(1, 1000) for _ in range(size)]
    
    start = time.perf_counter()
    selection_sort_simple(test_array.copy())
    elapsed = (time.perf_counter() - start) * 1000
    
    print(f"{size:<10} {elapsed:<20.4f}")

print("\nXUMANN: Selection Sort O(n²) murakkabligi tufayli katta massivlar uchun")
print("        unchalik tezlikli emas. Katta massivlar uchun Merge Sort (O(n log n))")
print("        yoki Quick Sort dan foydalanish tavsiya etiladi.")

