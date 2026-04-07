"""1-vazifa: Tub sonlarni parallel qidirish (multiprocessing) va ketma-ket variant bilan solishtirish."""

import multiprocessing
import time
import math


def tub_sonmi(n):
    """Sonning tub ekanligini tekshiradi."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i <= math.isqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def oraliqda_tub_sonlar(args):
    """Berilgan oraliqda tub sonlarni topadi."""
    boshlanish, tugash = args
    return [n for n in range(boshlanish, tugash) if tub_sonmi(n)]


def ketma_ket_qidirish(boshlanish, tugash):
    """Ketma-ket (oddiy) usulda tub sonlarni qidiradi."""
    return [n for n in range(boshlanish, tugash) if tub_sonmi(n)]


def parallel_qidirish(boshlanish, tugash, protsesslar_soni=4):
    """Multiprocessing yordamida tub sonlarni parallel qidiradi."""
    oraliq_uzunligi = (tugash - boshlanish) // protsesslar_soni
    oraliqlar = []
    for i in range(protsesslar_soni):
        oraliq_boshi = boshlanish + i * oraliq_uzunligi
        if i == protsesslar_soni - 1:
            oraliq_oxiri = tugash
        else:
            oraliq_oxiri = oraliq_boshi + oraliq_uzunligi
        oraliqlar.append((oraliq_boshi, oraliq_oxiri))

    with multiprocessing.Pool(processes=protsesslar_soni) as pool:
        natijalar = pool.map(oraliqda_tub_sonlar, oraliqlar)

    tub_sonlar = []
    for natija in natijalar:
        tub_sonlar.extend(natija)
    return tub_sonlar


if __name__ == "__main__":
    BOSHLANISH = 2
    TUGASH = 500_000

    # --- Ketma-ket qidirish ---
    vaqt_boshi = time.perf_counter()
    ketma_ket_natija = ketma_ket_qidirish(BOSHLANISH, TUGASH)
    ketma_ket_vaqt = time.perf_counter() - vaqt_boshi
    print(f"Ketma-ket: {len(ketma_ket_natija)} ta tub son topildi, vaqt: {ketma_ket_vaqt:.4f} s")

    # --- Parallel qidirish ---
    for protsesslar in [2, 4, 8]:
        vaqt_boshi = time.perf_counter()
        parallel_natija = parallel_qidirish(BOSHLANISH, TUGASH, protsesslar)
        parallel_vaqt = time.perf_counter() - vaqt_boshi
        tezlashuv = ketma_ket_vaqt / parallel_vaqt if parallel_vaqt > 0 else 0
        print(
            f"Parallel ({protsesslar} protsess): {len(parallel_natija)} ta tub son, "
            f"vaqt: {parallel_vaqt:.4f} s, tezlashuv: {tezlashuv:.2f}x"
        )

    # Tekshiruv
    assert len(ketma_ket_natija) == len(parallel_natija), "Natijalar mos kelmadi!"
    print("\nBirinchi 20 ta tub son:", ketma_ket_natija[:20])
