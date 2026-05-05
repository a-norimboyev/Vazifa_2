"""
7-amaliy topshiriq, 5-mavzu:
Matn shablonlari (RegEx)

Vazifa:
Matn ichidan +998 bilan boshlanuvchi telefon raqamlarini ajratib olish.
Faqat pattern deklaratsiyasi va regex qidiruvi ishlatiladi.
"""

import re

text = input("Matn kiriting: ").strip()

pattern = r"\+998(?:[\s-]?\d){9}"
phones = re.findall(pattern, text)

print("Topilgan telefon raqamlari:")
print(phones)
