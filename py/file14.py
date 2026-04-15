"""14-vazifa: Xanoy minorasi (Tower of Hanoi) — n ta diskni 3 ta ustun orqali ko'chirish."""


def xanoy_minorasi(n, manba="A", yordamchi="B", maqsad="C", qadamlar=None):
    """Xanoy minorasi algoritmini rekursiv hal qiladi.

    n ta diskni manba ustundan maqsad ustuniga yordamchi ustun orqali ko'chiradi.
    """
    if qadamlar is None:
        qadamlar = []

    if n == 1:
        qadam = f"Disk 1: {manba} → {maqsad}"
        qadamlar.append(qadam)
        return qadamlar

    # 1-qadam: n-1 ta diskni yordamchi ustuniga ko'chirish
    xanoy_minorasi(n - 1, manba, maqsad, yordamchi, qadamlar)

    # 2-qadam: Eng katta diskni maqsad ustuniga ko'chirish
    qadam = f"Disk {n}: {manba} → {maqsad}"
    qadamlar.append(qadam)

    # 3-qadam: n-1 ta diskni yordamchi ustunidan maqsadga ko'chirish
    xanoy_minorasi(n - 1, yordamchi, manba, maqsad, qadamlar)

    return qadamlar


def xanoy_vizual(n):
    """Xanoy minorasini vizual ko'rsatadi (ustunlar holatini bosqichma-bosqich)."""
    ustunlar = {"A": list(range(n, 0, -1)), "B": [], "C": []}
    qadam_raqam = 0

    def holat_chiqarish():
        nonlocal qadam_raqam
        print(f"\n  Qadam {qadam_raqam}:")
        max_balandlik = n
        for qator in range(max_balandlik, 0, -1):
            satr = "    "
            for ustun in ["A", "B", "C"]:
                if len(ustunlar[ustun]) >= qator:
                    disk = ustunlar[ustun][qator - 1]
                    satr += f" [{'█' * disk:^{n*2+1}}] "
                else:
                    satr += f" {'|':^{n*2+3}} "
            print(satr)
        print(f"    {'A':^{n*2+3}}  {'B':^{n*2+3}}  {'C':^{n*2+3}}")

    def kochirish(soni, manba, yordamchi, maqsad):
        nonlocal qadam_raqam
        if soni == 0:
            return
        kochirish(soni - 1, manba, maqsad, yordamchi)
        disk = ustunlar[manba].pop()
        ustunlar[maqsad].append(disk)
        qadam_raqam += 1
        print(f"\n  >>> Disk {disk}: {manba} → {maqsad}")
        holat_chiqarish()
        kochirish(soni - 1, yordamchi, manba, maqsad)

    print("  Boshlang'ich holat:")
    holat_chiqarish()
    kochirish(n, "A", "B", "C")


if __name__ == "__main__":
    print("=" * 55)
    print("XANOY MINORASI (Tower of Hanoi)")
    print("=" * 55)

    # Oddiy qadamlar ro'yxati
    for n in [2, 3, 4]:
        print(f"\n--- {n} ta disk ---")
        qadamlar = xanoy_minorasi(n)
        for i, qadam in enumerate(qadamlar, 1):
            print(f"  {i}. {qadam}")
        print(f"  Jami qadamlar: {len(qadamlar)} (formula: 2^{n}-1 = {2**n - 1})")

    # Vizual ko'rsatish (3 ta disk)
    print("\n" + "=" * 55)
    print("VIZUAL KO'RSATISH (3 ta disk)")
    print("=" * 55)
    xanoy_vizual(3)

    # Formulani ko'rsatish
    print("\n" + "=" * 55)
    print("XANOY MINORASI FORMULASI:")
    print("=" * 55)
    print("  Minimal qadamlar soni: 2^n - 1")
    for n in range(1, 11):
        print(f"  n={n:>2}: {2**n - 1:>6} qadam")
