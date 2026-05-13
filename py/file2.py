"""
7-amaliy topshiriq, 2-mavzu:
Ma'lumotlarni o'zgartirish (Map)

Talab:
Foydalanuvchi ismlari ro'yxatini qabul qilib,
ularni kattalashtirish va "ID-" prefiksi qo'shish.
map() funksiyasi va lambda dan foydalanish.
"""

raw_names = input("Ismlarni vergul bilan kiriting (masalan: ali,vali,sardor): ").strip()

names = list(
    filter(
        lambda name: name != "",
        map(lambda name: name.strip(), raw_names.split(",")),
    )
)

result = list(map(lambda name: f"ID-{name.upper()}", names))

print("\nNatija:")
if result:
    print("\n".join(result))
else:
    print("Hech qanday ism kiritilmadi.")
