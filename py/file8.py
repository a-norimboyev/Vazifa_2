"""8-vazifa: Map-Reduce modeli bilan statistik ko'rsatkichlarni hisoblash."""

import multiprocessing
import random
import math
import time


# ============================================================
# MAP bosqichi
# ============================================================
def map_funksiya(malumot_bolagi):
    """Har bir bo'lakdan lokal statistikani hisoblaydi (MAP)."""
    n = len(malumot_bolagi)
    if n == 0:
        return {"soni": 0, "yigindi": 0, "kvadrat_yigindi": 0,
                "minimum": float("inf"), "maksimum": float("-inf"),
                "saralangan": []}

    yigindi = sum(malumot_bolagi)
    kvadrat_yigindi = sum(x * x for x in malumot_bolagi)
    saralangan = sorted(malumot_bolagi)

    return {
        "soni": n,
        "yigindi": yigindi,
        "kvadrat_yigindi": kvadrat_yigindi,
        "minimum": saralangan[0],
        "maksimum": saralangan[-1],
        "saralangan": saralangan,
    }


# ============================================================
# REDUCE bosqichi
# ============================================================
def birlashtir_saralangan(chap, ong):
    """Ikki saralangan ro'yxatni birlashtiradi (merge)."""
    natija = []
    i = j = 0
    while i < len(chap) and j < len(ong):
        if chap[i] <= ong[j]:
            natija.append(chap[i])
            i += 1
        else:
            natija.append(ong[j])
            j += 1
    natija.extend(chap[i:])
    natija.extend(ong[j:])
    return natija


def reduce_funksiya(map_natijalari):
    """Barcha MAP natijalarini birlashtiradi (REDUCE)."""
    umumiy_soni = 0
    umumiy_yigindi = 0
    umumiy_kvadrat = 0
    umumiy_min = float("inf")
    umumiy_max = float("-inf")
    saralangan = []

    for natija in map_natijalari:
        if natija["soni"] == 0:
            continue
        umumiy_soni += natija["soni"]
        umumiy_yigindi += natija["yigindi"]
        umumiy_kvadrat += natija["kvadrat_yigindi"]
        umumiy_min = min(umumiy_min, natija["minimum"])
        umumiy_max = max(umumiy_max, natija["maksimum"])
        saralangan = birlashtir_saralangan(saralangan, natija["saralangan"])

    # O'rtacha
    ortacha = umumiy_yigindi / umumiy_soni if umumiy_soni > 0 else 0

    # Mediana
    if umumiy_soni == 0:
        mediana = 0
    elif umumiy_soni % 2 == 1:
        mediana = saralangan[umumiy_soni // 2]
    else:
        mediana = (saralangan[umumiy_soni // 2 - 1] + saralangan[umumiy_soni // 2]) / 2

    # Standart og'ish
    if umumiy_soni > 1:
        dispersiya = (umumiy_kvadrat - (umumiy_yigindi ** 2) / umumiy_soni) / (umumiy_soni - 1)
        standart_ogish = math.sqrt(max(0, dispersiya))
    else:
        standart_ogish = 0

    return {
        "soni": umumiy_soni,
        "ortacha": ortacha,
        "mediana": mediana,
        "standart_ogish": standart_ogish,
        "minimum": umumiy_min,
        "maksimum": umumiy_max,
    }


def map_reduce_statistika(malumotlar, protsesslar_soni=4):
    """Map-Reduce yordamida statistikani hisoblaydi."""
    # Ma'lumotlarni bo'laklarga bo'lish
    bolak_hajmi = len(malumotlar) // protsesslar_soni
    bolaklar = []
    for i in range(protsesslar_soni):
        boshi = i * bolak_hajmi
        oxiri = len(malumotlar) if i == protsesslar_soni - 1 else boshi + bolak_hajmi
        bolaklar.append(malumotlar[boshi:oxiri])

    # MAP — parallel
    with multiprocessing.Pool(protsesslar_soni) as pool:
        map_natijalari = pool.map(map_funksiya, bolaklar)

    # REDUCE — birlashtirish
    return reduce_funksiya(map_natijalari)


def oddiy_statistika(malumotlar):
    """Oddiy (ketma-ket) usulda statistikani hisoblaydi."""
    n = len(malumotlar)
    ortacha = sum(malumotlar) / n
    saralangan = sorted(malumotlar)
    if n % 2 == 1:
        mediana = saralangan[n // 2]
    else:
        mediana = (saralangan[n // 2 - 1] + saralangan[n // 2]) / 2
    dispersiya = sum((x - ortacha) ** 2 for x in malumotlar) / (n - 1)
    standart_ogish = math.sqrt(dispersiya)

    return {
        "soni": n,
        "ortacha": ortacha,
        "mediana": mediana,
        "standart_ogish": standart_ogish,
        "minimum": min(malumotlar),
        "maksimum": max(malumotlar),
    }


if __name__ == "__main__":
    HAJM = 1_000_000
    malumotlar = [random.gauss(50, 15) for _ in range(HAJM)]

    print("=" * 60)
    print(f"MAP-REDUCE STATISTIKA ({HAJM:,} ta element)")
    print("=" * 60)

    # Ketma-ket
    boshi = time.perf_counter()
    oddiy_natija = oddiy_statistika(malumotlar)
    oddiy_vaqt = time.perf_counter() - boshi

    # Map-Reduce
    boshi = time.perf_counter()
    mr_natija = map_reduce_statistika(malumotlar, protsesslar_soni=4)
    mr_vaqt = time.perf_counter() - boshi

    print(f"\n{'Ko`rsatkich':<20} {'Ketma-ket':>15} {'Map-Reduce':>15}")
    print("-" * 55)
    for kalit in ["soni", "ortacha", "mediana", "standart_ogish", "minimum", "maksimum"]:
        v1 = oddiy_natija[kalit]
        v2 = mr_natija[kalit]
        if isinstance(v1, float):
            print(f"{kalit:<20} {v1:>15.4f} {v2:>15.4f}")
        else:
            print(f"{kalit:<20} {v1:>15} {v2:>15}")

    tezlashuv = oddiy_vaqt / mr_vaqt if mr_vaqt > 0 else 0
    print(f"\nKetma-ket vaqt: {oddiy_vaqt:.4f} s")
    print(f"Map-Reduce vaqt: {mr_vaqt:.4f} s")
    print(f"Tezlashuv: {tezlashuv:.2f}x")
