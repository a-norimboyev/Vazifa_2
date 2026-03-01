"""
BLOK-SXEMA (MATNLI KO'RINISH) - ENG KICHIK ELEMENTNI TOPISH ALGORITMI
"""

print("=" * 75)
print("BLOK-SXEMA: ENG KICHIK ELEMENTNI TOPISH ALGORITMI")
print("=" * 75)

block_diagram = """
                    ┌──────────────┐
                    │  START       │
                    └──────┬───────┘
                           │
                    ┌──────▼──────────┐
                    │ array qabul qil │
                    └──────┬──────────┘
                           │
                    ┌──────▼──────────────────┐
                    │ min = array[0]; i = 1   │
                    └──────┬──────────────────┘
                           │
                    ┌──────▼──────────────────┐
                    │ i < len(array)?         │
                    └──────┬──────────────────┘
                    NO │          │ YES
                       │          │
                 ┌─────▼────┐  ┌──▼──────────────────┐
                 │ RETURN   │  │ array[i] < min?    │
                 │ min      │  └──┬──────────────────┘
                 └─────▲────┘     │
                       │    YES   │   NO
                       │   ┌──────┴────┐
                       │   │           │
                    ┌──┴───▼─┐  ┌──────▼────┐
                    │min =   │  │ i++       │
                    │array[i]│  └──────┬────┘
                    └──┬─────┘         │
                       │              │
                       │    ┌─────────┘
                       └────┴─────► (qayta sikl)
"""

print(block_diagram)

print("\n" + "=" * 75)
print("BLOK-SXEMA KOMPONENTLARINING TAVSIFI")
print("=" * 75)

description = """
┌─────────────────────────────────────────────────────────────────────────────┐
│                       BLOK-SXEMA ELEMENTLARI                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────┐  - START/END (Boshlanish/Tugatish nuqtasi)                       │
│  │ ORG  │                                                                   │
│  └──────┘                                                                   │
│                                                                             │
│  ┌─────────┐  - PROCESS (Operatsiya, hisoblash)                            │
│  │ Action  │    Misollar: min = array[0], i = 1                            │
│  └─────────┘                                                               │
│                                                                             │
│  ◇────────◇  - DECISION (Shart tekshirish, if-then-else)                   │
│   Shart?      Misollar: i < len(array)?, array[i] < min?                   │
│  ◇────────◇                                                                │
│                                                                             │
│  ────┬────    - FLOW LINE (Oqim yo'li, o'tish tartibi)                     │
│     │         YES/NO belgis bilan ko'rsatiladi                             │
│     ▼                                                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
"""

print(description)

print("\n" + "=" * 75)
print("QADAMMA-QADAM TUSHUNTIRISH")
print("=" * 75)

explanation = """
QADAM 1: START
   └─ Algoritm boshlanadi

QADAM 2: array qabul qil
   └─ Kiritilgan massiv qabul qilinadi
   └─ Misol: [5, 2, 9, 1, 7]

QADAM 3: min = array[0]; i = 1
   └─ Birinchi elementni eng kichik sifatida o'rnatamiz: min = 5
   └─ Sanagichni 1 dan boshlaymiz (2-elementdan tekshirish uchun)

QADAM 4: i < len(array)? [SHART TEKSHIRUVI]
   └─ Agar i massiv o'lchamidan kichik bo'lsa: YES (davom et)
   └─ Agar i massiv o'lchamiga teng yoki katta bo'lsa: NO (natija qaytarish)

QADAM 5 (YES holida): array[i] < min? [SHART TEKSHIRUVI]
   └─ Joriy element eng kichik elementdan kichik mi?
   ├─ YES: min = array[i] (yangi eng kichik topildi)
   └─ NO: o'zgartirishlarsiz davom et

QADAM 6: i++ [SANAGICHNI O'ZGARTIRISH]
   └─ Sanagichni 1 ga oshiramiz
   └─ Keyingi iteratsiyaga tashlanadi

QADAM 7: Sikl RETURN [QAYTA SHART TEKSHIRUVI]
   └─ QADAM 4 ga qaytamiz (i < len(array)?) ni qayta tekshiramiz

QADAM 8 (NO holida): RETURN min
   └─ Eng kichik element topilgan, natija qaytariladi
   └─ Algoritm tugaydi (END)
"""

print(explanation)

print("\n" + "=" * 75)
print("PRAKTIK MISOL: [5, 2, 9, 1, 7]")
print("=" * 75)

example = """
╔════╦═════════════════════════════════════════════════════════════════════╗
║ #  ║  TEKSHIRISH JARAYONI                                              ║
╠════╬═════════════════════════════════════════════════════════════════════╣
║ 1  ║  min = 5, i = 1                                                    ║
║    ║  1 < 5? → YES (davom)                                             ║
║    ║                                                                     ║
║ 2  ║  array[1] = 2 < 5? → YES!                                         ║
║    ║  min = 2  ← YANGIA OPT!                                            ║
║    ║  i = 2                                                             ║
║    ║  2 < 5? → YES (davom)                                             ║
║    ║                                                                     ║
║ 3  ║  array[2] = 9 < 2? → NO                                           ║
║    ║  min = 2 (o'zgarmadi)                                             ║
║    ║  i = 3                                                             ║
║    ║  3 < 5? → YES (davom)                                             ║
║    ║                                                                     ║
║ 4  ║  array[3] = 1 < 2? → YES!                                         ║
║    ║  min = 1  ← YANGIA OPT!                                            ║
║    ║  i = 4                                                             ║
║    ║  4 < 5? → YES (davom)                                             ║
║    ║                                                                     ║
║ 5  ║  array[4] = 7 < 1? → NO                                           ║
║    ║  min = 1 (o'zgarmadi)                                             ║
║    ║  i = 5                                                             ║
║    ║  5 < 5? → NO (TO'X!)                                              ║
║    ║                                                                     ║
║ 6  ║  RETURN min = 1                                                    ║
║    ║  ✓ NATIJA: Eng kichik element = 1                                 ║
╚════╩═════════════════════════════════════════════════════════════════════╝
"""

print(example)

print("\n" + "=" * 75)
print("MUHIM NUQTALAR")
print("=" * 75)

important = """
✓ SIKL SHARTI: i < len(array)
  └─ Massivning barcha elementlarini tekshirgunicha davom etadi

✓ AGAR SHART: array[i] < min_value
  └─ Eng kichik elementni eng kichikning yanara mavjud bo'lganini topadi

✓ QAYTA SIKL: (qayta shart tekshiruvi)
  └─ i++ bilan sanagich oshib, sikl qayta boshlanadi
  └─ Toki barcha elementlar tekshirilingunicha davom etadi

✗ MUMKIN BO'LGAN XATOLAR:
  ├─ Bo'sh massiv: IndexError (tekshirish kerak)
  ├─ Qayta sikl bo'lmasa: Birinchi element faqat qaytadi
  └─ Shart xato bo'lsa: Noto'g'ri eng kichik topiladi
"""

print(important)
