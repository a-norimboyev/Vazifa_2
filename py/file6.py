def is_palindrome(text):
    # 1. Matnni kichik harflarga o'tkazamiz va bo'shliqlarni olib tashlaymiz
    # Bu "Kiyik" yoki "A man a plan a canal Panama" kabi holatlarda to'g'ri ishlashi uchun kerak
    clean_text = "".join(text.split()).lower()
    
    # 2. Matnni o'zining teskarisi bilan solishtiramiz
    # [::-1] - bu Python-da qatorni teskari tartibda yozishning eng tez usuli
    return clean_text == clean_text[::-1]

# Sinab ko'ramiz:
test_words = ["kiyik", "olma", "radar", "Aziza", "Python"]

for word in test_words:
    print(f"{word} -> {is_palindrome(word)}")
