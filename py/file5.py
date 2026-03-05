# Psevdokod
"""
ALGORITM FindAnagrams(SozlarRoyxati)
    anagramlar_lugati = Yangi Lug'at (Hash Map)
    HAR BIR soz UCHUN (SozlarRoyxati ichidagi):
        saralangan_soz = saralash(soz)
        AGAR saralangan_soz lug'atda BO'LMASA:
            lug'at[saralangan_soz] = []
        lug'at[saralangan_soz].qo'shish(soz)
    NATIJA lug'at.qiymatlari()
OXIRI
"""
from collections import defaultdict

def find_anagrams(word_list):
    # defaultdict list bilan: agar kalit bo'lmasa, avtomat bo'sh list yaratadi
    anagram_map = defaultdict(list)
    
    for word in word_list:
        # So'zni kichik harfga o'tkazamiz va harflarini saralaymiz
        sorted_word = "".join(sorted(word.lower()))
        
        # Saralangan so'zni kalit sifatida ishlatamiz
        anagram_map[sorted_word].append(word)
    
    # Faqat guruhlangan so'zlarni qaytaramiz
    return list(anagram_map.values())

# Sinash
words = ["eat", "tea", "tan", "ate", "nat", "bat", "olma", "mola"]
result = find_anagrams(words)
print(result)
