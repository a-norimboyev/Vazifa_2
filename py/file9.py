def count_vowels(text):
    # Unli harflar to'plami (kichik harflarda)
    vowels = "aeiouo'"
    count = 0
    
    # Matndagi har bir belgini tekshiramiz
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

# Sinab ko'ramiz:
print(f"Unlilar soni: {count_vowels('Assalomu Alaykum')}") # Natija: 7
