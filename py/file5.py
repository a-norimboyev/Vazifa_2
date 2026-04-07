"""5-vazifa: Matritsalarni parallel ko'paytirish (multiprocessing)."""

import multiprocessing
import time
import random


def matritsa_yaratish(qatorlar, ustunlar, min_val=0, max_val=10):
    """Tasodifiy matritsa yaratadi."""
    return [[random.randint(min_val, max_val) for _ in range(ustunlar)] for _ in range(qatorlar)]


def matritsa_chiqarish(matritsa, nom="Matritsa", max_qator=6):
    """Matritsani chiroyli chiqaradi (katta matritsalar uchun qisqartirilgan)."""
    print(f"\n{nom} ({len(matritsa)}x{len(matritsa[0])}):")
    for i, qator in enumerate(matritsa):
        if i >= max_qator:
            print(f"  ... ({len(matritsa) - max_qator} ta qator tashlab qo'yildi)")
            break
        print(f"  {qator[:8]}{'...' if len(qator) > 8 else ''}")


def qator_kop(args):
    """Bitta qatorni butun B matritsasiga ko'paytiradi."""
    qator_indeksi, A_qator, B, B_ustunlar = args
    natija_qator = []
    for j in range(B_ustunlar):
        yigindi = 0
        for k in range(len(A_qator)):
            yigindi += A_qator[k] * B[k][j]
        natija_qator.append(yigindi)
    return (qator_indeksi, natija_qator)


def ketma_ket_kopaytirish(A, B):
    """Matritsalarni ketma-ket ko'paytiradi."""
    qatorlar_A = len(A)
    ustunlar_B = len(B[0])
    ichki = len(B)

    natija = [[0] * ustunlar_B for _ in range(qatorlar_A)]
    for i in range(qatorlar_A):
        for j in range(ustunlar_B):
            yigindi = 0
            for k in range(ichki):
                yigindi += A[i][k] * B[k][j]
            natija[i][j] = yigindi
    return natija


def parallel_kopaytirish(A, B, protsesslar_soni=4):
    """Matritsalarni parallel ko'paytiradi — qatorlarni jarayonlarga taqsimlaydi."""
    ustunlar_B = len(B[0])

    # Har bir qator uchun vazifa tayyorlash
    vazifalar = [(i, A[i], B, ustunlar_B) for i in range(len(A))]

    with multiprocessing.Pool(processes=protsesslar_soni) as pool:
        natijalar = pool.map(qator_kop, vazifalar)

    # Natijalarni tartiblash va matritsa shaklida yig'ish
    natijalar.sort(key=lambda x: x[0])
    return [qator for _, qator in natijalar]


if __name__ == "__main__":
    # Kichik namoyish
    print("=" * 60)
    print("KICHIK MATRITSA NAMOYISHI")
    print("=" * 60)

    A_kichik = matritsa_yaratish(3, 4)
    B_kichik = matritsa_yaratish(4, 3)
    matritsa_chiqarish(A_kichik, "A")
    matritsa_chiqarish(B_kichik, "B")

    natija = parallel_kopaytirish(A_kichik, B_kichik, 2)
    matritsa_chiqarish(natija, "A × B natija")

    # Katta matritsa solishtirish
    print("\n" + "=" * 60)
    print("KATTA MATRITSA SOLISHTIRISHI")
    print("=" * 60)

    for hajm in [100, 200, 300]:
        A = matritsa_yaratish(hajm, hajm)
        B = matritsa_yaratish(hajm, hajm)

        # Ketma-ket
        boshi = time.perf_counter()
        natija_ketma_ket = ketma_ket_kopaytirish(A, B)
        ketma_ket_vaqt = time.perf_counter() - boshi

        # Parallel
        boshi = time.perf_counter()
        natija_parallel = parallel_kopaytirish(A, B, protsesslar_soni=4)
        parallel_vaqt = time.perf_counter() - boshi

        tezlashuv = ketma_ket_vaqt / parallel_vaqt if parallel_vaqt > 0 else 0

        # Tekshiruv
        assert natija_ketma_ket == natija_parallel, "Natijalar mos kelmadi!"

        print(
            f"  {hajm}x{hajm}: ketma-ket={ketma_ket_vaqt:.3f}s, "
            f"parallel={parallel_vaqt:.3f}s, tezlashuv={tezlashuv:.2f}x"
        )
