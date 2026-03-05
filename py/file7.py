#  (for sikli yordamida)
def calculate_factorial(n):
    # Manfiy sonlar uchun faktorial mavjud emas
    if n < 0:
        return "Xato: Manfiy son kiritildi"
    
    result = 1
    # 1 dan n gacha bo'lgan barcha sonlarni ko'paytirib chiqamiz
    for i in range(1, n + 1):
        result *= i
        
    return result

# Sinab ko'ramiz:
number = 5
print(f"{number}! = {calculate_factorial(number)}") # Natija: 120

# Rekursiv usul (Funksiya o'zini chaqirishi orqali)
"""
def calculate_factorial_recursive(n):
    if n < 0:
        return "Xato"
    # To'xtash sharti: 0! va 1! har doim 1 ga teng
    if n == 0 or n == 1:
        return 1
    
    return n * calculate_factorial_recursive(n - 1)

"""
# (Python kutubxonasi yordamida)
"""
import math

n = 5
print(math.factorial(n))
"""