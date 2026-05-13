"""
7-amaliy topshiriq, 3-mavzu:
Ro'yxat tushunchasi (List Comprehension)

Talab:
1 dan 100 gacha sonlar ichidan ham 3 ga, ham 5 ga bo'linadigan
sonlarning kvadratini faqat bitta qatorda List Comprehension bilan yozish.
"""

result = [n**2 for n in range(1, 101) if n % 3 == 0 and n % 5 == 0]
numbers = [n for n in range(1, 101) if n % 3 == 0 and n % 5 == 0]

print("Natija:")
print("Bo'linadigan sonlar:")
print(numbers)
print("Kvadratlari:")
print(result)
