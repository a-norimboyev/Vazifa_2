"""16-vazifa: Papka ichidagi barcha fayllarni rekursiya yordamida hisoblash."""

import os
import time


def fayllarni_hisoblash(papka_yoli):
    """Papka va uning barcha ichki papkalaridagi fayllarni rekursiv hisoblaydi.

    Qaytaradi: (fayllar_soni, papkalar_soni, umumiy_hajm)
    """
    fayllar_soni = 0
    papkalar_soni = 0
    umumiy_hajm = 0

    try:
        elementlar = os.listdir(papka_yoli)
    except PermissionError:
        return 0, 0, 0

    for element in elementlar:
        toliq_yol = os.path.join(papka_yoli, element)

        if os.path.isfile(toliq_yol):
            fayllar_soni += 1
            try:
                umumiy_hajm += os.path.getsize(toliq_yol)
            except OSError:
                pass
        elif os.path.isdir(toliq_yol):
            papkalar_soni += 1
            # Rekursiv chaqiruv — ichki papkani ham hisoblash
            ichki_fayllar, ichki_papkalar, ichki_hajm = fayllarni_hisoblash(toliq_yol)
            fayllar_soni += ichki_fayllar
            papkalar_soni += ichki_papkalar
            umumiy_hajm += ichki_hajm

    return fayllar_soni, papkalar_soni, umumiy_hajm


def hajm_formatlash(baytlar):
    """Baytlarni odam o'qiy oladigan formatga o'zgartiradi."""
    birliklar = ["B", "KB", "MB", "GB", "TB"]
    indeks = 0
    hajm = float(baytlar)
    while hajm >= 1024 and indeks < len(birliklar) - 1:
        hajm /= 1024
        indeks += 1
    return f"{hajm:.2f} {birliklar[indeks]}"


def papka_daraxtini_chiqarish(papka_yoli, cheklov="", chuqurlik=0, max_chuqurlik=3):
    """Papka daraxtini chiroyli ko'rsatadi (rekursiv)."""
    if chuqurlik > max_chuqurlik:
        return

    try:
        elementlar = sorted(os.listdir(papka_yoli))
    except PermissionError:
        print(f"{cheklov}[Ruxsat yo'q]")
        return

    fayllar = [e for e in elementlar if os.path.isfile(os.path.join(papka_yoli, e))]
    papkalar = [e for e in elementlar if os.path.isdir(os.path.join(papka_yoli, e))]

    for i, papka in enumerate(papkalar):
        oxirgi = (i == len(papkalar) - 1) and len(fayllar) == 0
        belgi = "└── " if oxirgi else "├── "
        print(f"{cheklov}{belgi}📁 {papka}/")
        keyingi_cheklov = cheklov + ("    " if oxirgi else "│   ")
        papka_daraxtini_chiqarish(
            os.path.join(papka_yoli, papka), keyingi_cheklov, chuqurlik + 1, max_chuqurlik
        )

    for i, fayl in enumerate(fayllar):
        oxirgi = i == len(fayllar) - 1
        belgi = "└── " if oxirgi else "├── "
        toliq_yol = os.path.join(papka_yoli, fayl)
        try:
            hajm = os.path.getsize(toliq_yol)
        except OSError:
            hajm = 0
        print(f"{cheklov}{belgi}📄 {fayl} ({hajm_formatlash(hajm)})")


def kengaytma_statistikasi(papka_yoli):
    """Fayl kengaytmalari bo'yicha statistika (rekursiv)."""
    statistika = {}

    try:
        elementlar = os.listdir(papka_yoli)
    except PermissionError:
        return statistika

    for element in elementlar:
        toliq_yol = os.path.join(papka_yoli, element)

        if os.path.isfile(toliq_yol):
            _, kengaytma = os.path.splitext(element)
            kengaytma = kengaytma.lower() if kengaytma else "(kengaytmasiz)"
            if kengaytma not in statistika:
                statistika[kengaytma] = {"soni": 0, "hajm": 0}
            statistika[kengaytma]["soni"] += 1
            try:
                statistika[kengaytma]["hajm"] += os.path.getsize(toliq_yol)
            except OSError:
                pass
        elif os.path.isdir(toliq_yol):
            ichki = kengaytma_statistikasi(toliq_yol)
            for k, v in ichki.items():
                if k not in statistika:
                    statistika[k] = {"soni": 0, "hajm": 0}
                statistika[k]["soni"] += v["soni"]
                statistika[k]["hajm"] += v["hajm"]

    return statistika


if __name__ == "__main__":
    # Joriy loyiha papkasini tekshirish
    papka = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    print("=" * 55)
    print(f"PAPKA TAHLILI: {papka}")
    print("=" * 55)

    # 1. Fayllarni hisoblash
    boshi = time.perf_counter()
    fayllar, papkalar_s, hajm = fayllarni_hisoblash(papka)
    vaqt = time.perf_counter() - boshi

    print(f"\n📊 Umumiy statistika:")
    print(f"   Fayllar soni:   {fayllar}")
    print(f"   Papkalar soni:  {papkalar_s}")
    print(f"   Umumiy hajm:    {hajm_formatlash(hajm)}")
    print(f"   Hisoblash vaqti: {vaqt:.4f} s")

    # 2. Papka daraxti
    print(f"\n📂 Papka daraxti (3 chuqurlikkacha):")
    print(f"   {os.path.basename(papka)}/")
    papka_daraxtini_chiqarish(papka, "   ", max_chuqurlik=3)

    # 3. Kengaytma statistikasi
    print(f"\n📋 Kengaytma bo'yicha statistika:")
    statistika = kengaytma_statistikasi(papka)
    saralangan = sorted(statistika.items(), key=lambda x: x[1]["soni"], reverse=True)
    print(f"   {'Kengaytma':<15} {'Soni':>6} {'Hajm':>12}")
    print("   " + "-" * 35)
    for kengaytma, malumot in saralangan:
        print(f"   {kengaytma:<15} {malumot['soni']:>6} {hajm_formatlash(malumot['hajm']):>12}")
