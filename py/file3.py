def is_prime_naive(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Optimallashtirilgan algoritm
"""
import math

def is_prime_optimized(n):
    if n < 2: return False
    if n == 2: return True  # 2 - yagona juft tub son
    if n % 2 == 0: return False # Qolgan barcha juft sonlar tub emas
    
    # Faqat ildizigacha va faqat toq sonlarni tekshiramiz
    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True
"""