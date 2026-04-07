"""4-vazifa: Parallel qo'shib saralash (merge sort) va tezlashuv o'lchash."""

import multiprocessing
import time
import random


def birlashtir(chap, ong):
    """Ikki tartiblangan ro'yxatni birlashtiradi."""
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


def merge_sort(massiv):
    """Oddiy merge sort (ketma-ket)."""
    if len(massiv) <= 1:
        return massiv
    orta = len(massiv) // 2
    chap = merge_sort(massiv[:orta])
    ong = merge_sort(massiv[orta:])
    return birlashtir(chap, ong)


def parallel_merge_sort(massiv, chuqurlik=0, max_chuqurlik=2):
    """Parallel merge sort — chuqurlikni cheklash bilan."""
    if len(massiv) <= 1:
        return massiv

    orta = len(massiv) // 2

    if chuqurlik < max_chuqurlik:
        # Parallel bajarish
        with multiprocessing.Pool(2) as pool:
            chap_natija = pool.apply_async(parallel_merge_sort, (massiv[:orta], chuqurlik + 1, max_chuqurlik))
            ong_natija = pool.apply_async(parallel_merge_sort, (massiv[orta:], chuqurlik + 1, max_chuqurlik))
            chap = chap_natija.get()
            ong = ong_natija.get()
    else:
        # Ketma-ket bajarish (chuqurlik chegarasida)
        chap = merge_sort(massiv[:orta])
        ong = merge_sort(massiv[orta:])

    return birlashtir(chap, ong)


def oddiy_parallel_sort(massiv, protsesslar_soni=4):
    """Massivni bo'laklarga bo'lib, parallel saralab, keyin birlashtiradi."""
    uzunlik = len(massiv)
    bolak_hajmi = uzunlik // protsesslar_soni
    bolaklar = []
    for i in range(protsesslar_soni):
        boshi = i * bolak_hajmi
        oxiri = uzunlik if i == protsesslar_soni - 1 else boshi + bolak_hajmi
        bolaklar.append(massiv[boshi:oxiri])

    with multiprocessing.Pool(protsesslar_soni) as pool:
        saralangan_bolaklar = pool.map(merge_sort, bolaklar)

    # Barcha saralangan bo'laklarni birlashtirish
    natija = saralangan_bolaklar[0]
    for i in range(1, len(saralangan_bolaklar)):
        natija = birlashtir(natija, saralangan_bolaklar[i])
    return natija


def tezlashuvni_olchash(massiv_hajmi, protsesslar=4):
    """Ketma-ket va parallel saralashni solishtiradi."""
    massiv = [random.randint(1, 1_000_000) for _ in range(massiv_hajmi)]

    # Ketma-ket
    nusxa1 = massiv.copy()
    boshi = time.perf_counter()
    ketma_ket_natija = merge_sort(nusxa1)
    ketma_ket_vaqt = time.perf_counter() - boshi

    # Parallel
    nusxa2 = massiv.copy()
    boshi = time.perf_counter()
    parallel_natija = oddiy_parallel_sort(nusxa2, protsesslar)
    parallel_vaqt = time.perf_counter() - boshi

    tezlashuv = ketma_ket_vaqt / parallel_vaqt if parallel_vaqt > 0 else 0

    # Tekshiruv
    assert ketma_ket_natija == parallel_natija, "Natijalar mos kelmadi!"

    return ketma_ket_vaqt, parallel_vaqt, tezlashuv


if __name__ == "__main__":
    hajmlar = [10_000, 50_000, 100_000, 200_000]

    print(f"{'Massiv hajmi':>15} | {'Ketma-ket (s)':>14} | {'Parallel (s)':>13} | {'Tezlashuv':>10}")
    print("-" * 65)

    for hajm in hajmlar:
        ketma_ket, parallel, tezlashuv = tezlashuvni_olchash(hajm)
        print(f"{hajm:>15,} | {ketma_ket:>14.4f} | {parallel:>13.4f} | {tezlashuv:>9.2f}x")
