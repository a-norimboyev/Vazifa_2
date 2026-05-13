"""
7-amaliy topshiriq, 9-mavzu:
Shartli hisob-kitoblar (Dict Comprehension)

Vazifa:
Mahsulot narxlariga 10% chegirma qo'llab,
yangi lug'at hosil qilish.
"""

products = {
    "olma": 12000,
    "banan": 18000,
    "anor": 25000,
    "uzum": 0,
}

discounted_products = {
    name: round(price * 0.9, 2)
    for name, price in products.items()
    if price > 0
}

print("Asl narxlar:")
print(products)
print("\nChegirmali narxlar:")
print(discounted_products)
