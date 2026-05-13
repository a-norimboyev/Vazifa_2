"""
7-amaliy topshiriq, 7-mavzu:
Dekoratorlar (Meta-programming)

Vazifa:
Funksiya ishga tushishidan oldin log chiqaruvchi dekorator yaratish.
"""


def logger(func):
    def wrapper(*args, **kwargs):
        print("Log: Funksiya chaqirildi")
        return func(*args, **kwargs)

    return wrapper


@logger
def salom_ber(ism: str) -> str:
    return f"Salom, {ism}!"


ism = input("Ismingizni kiriting: ").strip()
print(salom_ber(ism))
