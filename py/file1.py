"""
VAZIFA 1: Oddiy algoritmni loyihalash - Massivdagi eng kichik elementni topish

VERBAL TAVSIF:
Algoritmni amalga oshirish uchun massivning birinchi elementini eng kichik sifatida o'rnatamiz.
Keyin massivning qolgan elementlari bilan taqqoslaydi, agar hozirgi element eng kichik 
elementi kichik bo'lsa, uni yangi eng kichik element sifatida o'rnatamiz.

PSEVDOKOD:
┌─────────────────────────────────────────┐
│ ALGORITM: Find_Minimum(array)           │
│ INPUT: array - sonlar massivi           │
│ OUTPUT: min_value - eng kichik element  │
│                                         │
│ 1. min_value ← array[0]                 │
│ 2. i ← 1                                │
│ 3. WHILE i < array.length DO            │
│ 4.    IF array[i] < min_value THEN      │
│ 5.       min_value ← array[i]           │
│ 6.    END IF                            │
│ 7.    i ← i + 1                         │
│ 8. END WHILE                            │
│ 9. RETURN min_value                     │
└─────────────────────────────────────────┘

BLOK-SXEMA: Alohida faylga ko'chib o'tdi → blok_sxema.py
(Fayl ishga tushirish: python py/blok_sxema.py)


# PYTHON KODI
def find_minimum(array):
    """Massivdagi eng kichik elementni topadi"""
    if not array:
        return None
    
    min_value = array[0]
    for i in range(1, len(array)):
        if array[i] < min_value:
            min_value = array[i]
    
    return min_value


# TRASSIROVKA (Step-by-step execution) - [5, 2, 9, 1, 7] uchun
print("=" * 60)
print("VASIFA 1: ENG KICHIK ELEMENTNI TOPISH")
print("=" * 60)

array = [5, 2, 9, 1, 7]
print(f"\nBoshlang'ich massiv: {array}")
print("\nTRASSIROVKA (Qadamma-qadam ishlash):")
print("-" * 60)

min_value = array[0]
print(f"Qadam 1: min_value = array[0] = {min_value}")

for i in range(1, len(array)):
    print(f"\nQadam {i+1}: array[{i}] = {array[i]} ni tavsiflang")
    if array[i] < min_value:
        print(f"         {array[i]} < {min_value} ✓ (to'g'ri)")
        min_value = array[i]
        print(f"         min_value yangilandi: {min_value}")
    else:
        print(f"         {array[i]} < {min_value} ✗ (noto'g'ri)")
        print(f"         min_value o'zgarishsiz qoldi: {min_value}")

print("\n" + "=" * 60)
print(f"NATIJA: Eng kichik element = {min_value}")
print("=" * 60)

# Hamjamiyat tekshirish
result = find_minimum(array)
print(f"\nFunksiya natijasi: {result}")
print(f"Python built-in min() natijasi: {min(array)}")
print(f"Natijalar mos keladi: {result == min(array)}")

