"""
7-amaliy topshiriq, 4-mavzu:
Ma'lumotlar bazasi bilan ishlash (Pandas)

Talab:
Jadvaldagi ma'lumotlarni shahar bo'yicha guruhlab,
har bir shahar uchun o'rtacha ish haqini hisoblash.
Deklarativ usul: df.groupby('city')['salary'].mean()
"""

import pandas as pd

count = int(input("Nechta xodim ma'lumotini kiritasiz? ").strip())

names = []
cities = []
salaries = []

for i in range(1, count + 1):
    print(f"\n{i}-xodim:")
    names.append(input("Ismi: ").strip())
    cities.append(input("Shahri: ").strip())
    salaries.append(float(input("Maoshi: ").strip()))

data = {"name": names, "city": cities, "salary": salaries}

df = pd.DataFrame(data)

average_salary_by_city = df.groupby("city")["salary"].mean()

print("Jadval:")
print(df)
print("\nShahar bo'yicha o'rtacha ish haqi:")
print(average_salary_by_city)
