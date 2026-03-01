"""
VAZIFA 5: ANAGRAMMALARNI TOPISH ALGORITMI
KOMPLEKS MASALA - TO'LIQ LOYIHALASH SIKLI

TAHLIL → USULNI TANLASH → PSEVDOKOD → AMALGA OSHIRISH → TESTLASH → MURAKKABLIKNI BAHOLASH
"""

from collections import defaultdict
from typing import List, Dict
import time

print("=" * 80)
print("VAZIFA 5: ANAGRAMMALARNI TOPISH ALGORITMI - TO'LIQ LOYIHALASH SIKLI")
print("=" * 80)

# ============================================================================
# 1. TAHLIL (ANALIZ)
# ============================================================================
print("\n1. TAHLIL (PROBLEM ANALYSIS)")
print("-" * 80)

print("""
MUAMMO: So'zlar ro'yxatidan barcha anagramma guruhlarini topish

ANAGRAMMA: Bir xil harflardan tuzilgan, lekin boshqa tartibda yozilgan so'zlar
  Misol: "listen" va "silent" - anogramma
         "evil" va "vile" - anogramma

MUAMMONING QISMLAR:
1. Anagrammalar tufayli qaysi so'zlar bir-biriga aloqadorligi?
   → YECHIM: Bir xil harflarni tartiblab qo'ysak, ularning identifikatori bo'ladi
   
2. Bir-biriga anogramma bo'lgan so'zlarni qanday guruhlash?
   → YECHIM: Har bir so'z uchun "kalit" (sorted characters) hisoblash
            Keyin ayni bir kalitga ega bo'lgan so'zlarni guruhlash
            
3. Natijani qanday taqdim etish?
   → YECHIM: Dictionary: kalit → so'zlar ro'yxati

MISOLLAR:
Input:  ['listen', 'silent', 'hello', 'world', 'evil', 'vile', 'elhi']
Output: {
  'eilnst': ['listen', 'silent', 'enlist'],
  'ellho': ['hello'],
  'dlorw': ['world'],
  'eilv': ['evil', 'vile', 'live'],
  'ehil': ['elhi', 'heli']
}
""")

# ============================================================================
# 2. USULNI TANLASH
# ============================================================================
print("\n2. USULNI TANLASH")
print("-" * 80)

print("""
VARIANTLAR:

A) SORTING ORQALI (TAVSIYA ETILGAN):
   ├─ Har bir so'z uchun harflarni o'lchamini tartiblab qo'y
   ├─ Tartiblab qo'yilgan harflar satrini kalit sifatida ishlatish
   ├─ Dictionary-ga qo'shish
   └─ Murakkabligi: O(n · m·log m) - n = so'zlar, m = o'rtacha so'z uzunligi

B) HASH (HISOBLASH) ORQALI:
   ├─ Har bir harfning soni uchun tuple yaratish
   ├─ Tuple-ni kalit sifatida ishlatish
   └─ Murakkabligi: O(n · m)

C) BRUTE FORCE (KUCHLI USUL):
   ├─ Har bir juft so'zni taqqoslash
   ├─ Har bir para uchun o'rinviy ruxsatlarni tekshirish
   └─ Murakkabligi: O(n² · m!) - o'tib qolgan sekin!

TANLANDI: A) SORTING (Sodda va samarali)
""")

# ============================================================================
# 3. PSEVDOKOD
# ============================================================================
print("\n3. PSEVDOKOD")
print("-" * 80)

print("""
PSEVDOKOD:
┌──────────────────────────────────────────────────────────────┐
│ ALGORITM: FindAnagrams(word_list)                            │
│ INPUT: word_list - so'zlar ro'yxati                          │
│ OUTPUT: groupedWord - anagrammar guruhed                     │
│                                                              │
│ 1. anagram_groups ← empty dictionary                         │
│ 2. FOR EACH word IN word_list DO                             │
│ 3.    // So'zning harflarini tartiblab qo'y                  │
│ 4.    sorted_word ← SORT_CHARACTERS(word)                    │
│ 5.                                                            │
│ 6.    // Agar bu kalit dictionary-da yo'q bo'lsa, yaratish   │
│ 7.    IF sorted_word NOT IN anagram_groups THEN              │
│ 8.       anagram_groups[sorted_word] ← empty list            │
│ 9.    END IF                                                  │
│ 10.   // So'zni ro'yxatga qo'shish                           │
│ 11.   anagram_groups[sorted_word].APPEND(word)               │
│ 12. END FOR                                                   │
│ 13. RETURN anagram_groups                                    │
└──────────────────────────────────────────────────────────────┘

YORDAMCHI FUNKSIYA:
┌──────────────────────────────────────────────────────────────┐
│ FUNKSIYA: SORT_CHARACTERS(word)                              │
│ INPUT: word - so'z                                           │
│ OUTPUT: sorted_chars - tartiblab qo'yilgan harflar           │
│                                                              │
│ 1. chars ← CONVERT_TO_ARRAY(word)                            │
│ 2. SORT(chars)                               // O(m·log m)   │
│ 3. RETURN JOIN_TO_STRING(chars)                              │
└──────────────────────────────────────────────────────────────┘
""")

# ============================================================================
# 4. AMALGA OSHIRISH (IMPLEMENTATION)
# ============================================================================
print("\n4. AMALGA OSHIRISH (IMPLEMENTATION)")
print("-" * 80)

def find_anagrams(words: List[str]) -> Dict[str, List[str]]:
    """
    So'zlar ro'yxatidan anagrammalarni guruhlash
    
    Args:
        words: So'zlar ro'yxati
    
    Returns:
        Anagrammar guruhlari (kalit: harflar, qiymat: so'zlar)
    """
    anagram_groups = defaultdict(list)
    
    for word in words:
        # Har bir so'z uchun harflarni tartiblab qo'y
        sorted_word = ''.join(sorted(word.lower()))
        
        # Keltirilgan kalitni guruppa-ga qo'shish
        anagram_groups[sorted_word].append(word)
    
    return dict(anagram_groups)


def find_anagrams_verbose(words: List[str]) -> Dict[str, List[str]]:
    """Qadamma-qadam ishlashini ko'rsatadigan versiya (o'quv uchun)"""
    anagram_groups = defaultdict(list)
    
    print("\nQadamma-qadam ishlash:")
    for i, word in enumerate(words, 1):
        sorted_word = ''.join(sorted(word.lower()))
        anagram_groups[sorted_word].append(word)
        print(f"  {i}. '{word}' → kalit: '{sorted_word}'")
    
    return dict(anagram_groups)

# ============================================================================
# 5. TESTLASH
# ============================================================================
print("\n5. TESTLASH")
print("-" * 80)

# TEST 1: Asosiy test
print("\n--- TEST 1: Asosiy misol ---")
test1 = ['listen', 'silent', 'hello', 'world', 'evil', 'vile', 'live']
print(f"Input: {test1}")
result1 = find_anagrams_verbose(test1)
print(f"\nNatija:")
for key, words in sorted(result1.items()):
    print(f"  '{key}': {words}")

# TEST 2: Minimal test
print("\n" + "-" * 80)
print("\n--- TEST 2: Bo'sh ro'yxat ---")
test2 = []
result2 = find_anagrams(test2)
print(f"Input: {test2}")
print(f"Natija: {result2}")
print(f"To'g'ri: {result2 == {}}")

# TEST 3: Bitta so'z
print("\n--- TEST 3: Bitta so'z ---")
test3 = ['heart']
result3 = find_anagrams(test3)
print(f"Input: {test3}")
print(f"Natija: {result3}")
print(f"To'g'ri: {len(result3) == 1}")

# TEST 4: Hamma anagramma
print("\n--- TEST 4: Hamma anagramma ---")
test4 = ['abc', 'bca', 'cab', 'acb', 'bac', 'cba']
result4 = find_anagrams(test4)
print(f"Input: {test4}")
print(f"Natija: {result4}")
print(f"To'g'ri: {len(result4) == 1 and len(list(result4.values())[0]) == 6}")

# TEST 5: Hech kimdir anagramma emas
print("\n--- TEST 5: Hech kimdir anagramma emas ---")
test5 = ['apple', 'banana', 'cherry', 'date']
result5 = find_anagrams(test5)
print(f"Input: {test5}")
print(f"Natija:")
for key, words in sorted(result5.items()):
    print(f"  '{key}': {words}")
print(f"To'g'ri: {len(result5) == 4}")

# TEST 6: Bosh o'rinlar va har xil o'lcham harflari
print("\n--- TEST 6: Har xil o'lcham harflari (CASE INSENSITIVE) ---")
test6 = ['Listen', 'SILENT', 'hello']
result6 = find_anagrams(test6)
print(f"Input: {test6}")
print(f"Natija:")
for key, words in sorted(result6.items()):
    print(f"  '{key}': {words}")

# TEST 7: Katta ro'yxat
print("\n--- TEST 7: Katta ro'yxat (1000 so'z) ---")
import random
words_large = [''.join(random.sample('abcdefghij', 5)) for _ in range(1000)]
# Ayni bir so'zdan anagrammalarni qo'shish
words_large.extend([''.join(sorted(words_large[0])), ''.join(sorted(words_large[1]))])
result7 = find_anagrams(words_large)
print(f"Input: {len(words_large)} so'z")
print(f"Natija: {len(result7)} turli xil anogramma guruhi")
print(f"Eng katta guruh: {max(len(v) for v in result7.values())} so'z")

# ============================================================================
# 6. MURAKKABLIKNI BAHOLASH
# ============================================================================
print("\n" + "=" * 80)
print("6. MURAKKABLIKNI BAHOLASH")
print("-" * 80)

print("""
VAQT MURAKKABLIGI TAHLILI:
┌─────────────────────────────────────────────────────────────┐
│ 1. Har bir so'z uchun harflarni tartiblab qo'y: O(m·log m)  │
│    (m = so'zning o'rtacha uzunligi)                          │
│                                                             │
│ 2. n ta so'z bor: O(n)                                       │
│                                                             │
│ 3. UMUMIY: O(n · m·log m)                                    │
│    n = so'zlar soni                                          │
│    m = o'rtacha so'z uzunligi                                │
│                                                             │
│ PRAKTIKADA: m o'zgarchaga kichik bo'lganidagi usullari       │
│             ba'zida O(n · m) hisoblanadi                     │
└─────────────────────────────────────────────────────────────┘

JOYNI ISHLATISH:
├─ Dictionary: O(n) (n anogramma guruhi)
├─ Sorted harflar: O(m)
└─ UMUMIY: O(n + m)

SAMARADORLIK TAQQOSLASH:
┌─────────────────────────────────────────────────────────────┐
│ Usuli         │ Vaqt           │ Joy  │ Qullay │ Murakkablik│
├───────────────┼────────────────┼──────┼────────┼────────────┤
│ Sorting       │ O(n·m·log m)   │ O(n) │ ✓✓✓   │ Orta       │
│ Hash Count    │ O(n·m)         │ O(n) │ ✓✓    │ Orta       │
│ Brute Force   │ O(n²·m!)       │ O(1) │ ✗✗✗   │ Juda murk. │
└─────────────────────────────────────────────────────────────┘

TAVSIYALAR:
✓ SORTING usuli eng yaxshi - sodda, tezlik, oson
✓ HASH COUNT usuli - ch'okray yam amalda
✗ BRUTE FORCE - faqat ochroq masalalar uchun
""")

# ============================================================================
# 7. ISHLASH TEZLIGINI TAQQOSLASH
# ============================================================================
print("\n" + "=" * 80)
print("7. ISHLASH TEZLIGINI TAQQOSLASH")
print("-" * 80)

import random
import string

def generate_random_words(count, length=5):
    """Tasodifiy so'zlar yaratish"""
    return [''.join(random.choices(string.ascii_lowercase, k=length)) 
            for _ in range(count)]

# Sorting usuli
def find_anagrams_sort(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word.lower()))
        groups[key].append(word)
    return dict(groups)

# Hash Count usuli
def find_anagrams_hash(words):
    groups = defaultdict(list)
    for word in words:
        # Harflar soni tuple
        char_count = tuple(sorted([(c, word.lower().count(c)) 
                                   for c in set(word.lower())]))
        groups[char_count].append(word)
    return dict(groups)

sizes = [100, 500, 1000, 5000]
print(f"\n{'Hajm':<10} {'Sorting (ms)':<15} {'Hash Count (ms)':<15}")
print("-" * 40)

for size in sizes:
    test_words = generate_random_words(size)
    
    # Sorting
    start = time.perf_counter()
    find_anagrams_sort(test_words)
    sort_time = (time.perf_counter() - start) * 1000
    
    # Hash Count
    start = time.perf_counter()
    find_anagrams_hash(test_words)
    hash_time = (time.perf_counter() - start) * 1000
    
    print(f"{size:<10} {sort_time:<15.4f} {hash_time:<15.4f}")

# ============================================================================
# 8. YANADA TAKOMIL MISOL
# ============================================================================
print("\n" + "=" * 80)
print("8. YANADA TAKOMIL MISOL - INGLIZ TILI SO'ZLARI BILAN")
print("=" * 80)

english_words = [
    'listen', 'silent', 'enlist',
    'evil', 'vile', 'live',
    'heart', 'earth', 'hater',
    'dessert', 'stressed',
    'atlas', 'slat', 'salt', 'last',
    'dormitory', 'dirty room',
    'astronomer', 'moon starer',
    'hello', 'world'
]

print(f"\nKiritilgan so'zlar: {english_words}")
result_english = find_anagrams(english_words)

print(f"\nAnogrammar guruhlari:")
group_num = 1
for key, words in sorted(result_english.items()):
    if len(words) > 1:
        print(f"  Guruh {group_num}: {words}")
        group_num += 1

print(f"\nJami anogramma guruhlari: {len(result_english)}")
print(f"Anogramma bo'lgan so'zlar: {sum(1 for words in result_english.values() if len(words) > 1)}")

# ============================================================================
# 9. XULOSA
# ============================================================================
print("\n" + "=" * 80)
print("9. XULOSA VA XULOSA")
print("=" * 80)

print("""
LOYIHALASH SIKLI RINGDANMASI:

✓ TAHLIL:      Muammoni chuqur tushunish
✓ USUL TANLASH: Sorting usuli tanlandi (sodda, samarali)
✓ PSEVDOKOD:   Algoritmi logikasi belgilandi
✓ AMALGA:      Python kodida ishlashtirildi
✓ TESTLASH:    Har xil holatlar tekshirildi
✓ BAHOLASH:    O(n·m·log m) murakkabligi aniqland

ASOSIY O'RGANISHLAR:
1. Anogramma: Bir xil harflardan tuzilgan so'zlar
2. Kalit tizimi: 'sorted characters' kalit sifatida
3. Dictionary grouping: Monivator tushunchasini amalga oshirish
4. Case insensitive: Bosh/kichik harflarni birlashtirish

PRACTICAL QOLANMALAR:
✓ Kontestlar: Anogramma topish masalalari tez-tez bo'ladi
✓ Interview: Bu mantiqiy va algoritmik bilim ko'rsatadi
✓ Real dunyo: Plagiarism detection, spell checker, tavsiya sistemas

BUNDAN KEYINGI QADAM:
- Katta malumotlarni qidirish (Trie struktura)
- O'rta va katta massivlar bilan ishlash (indeksing)
- Parallel processing (bir vaqtning o'zida ishlash)
""")

