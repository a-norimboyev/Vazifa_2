"""11-vazifa: Rekursiv algoritmlar — faktorial, Fibonachchi, ma'lumotlar strukturasini kesib o'tish."""


# ============================================================
# 1. FAKTORIAL
# ============================================================
def faktorial(n):
    """n! ni rekursiv hisoblaydi."""
    if n <= 1:
        return 1
    return n * faktorial(n - 1)


# ============================================================
# 2. FIBONACHCHI SONLARI (memoizatsiya bilan)
# ============================================================
def fibonachchi(n, xotira={}):
    """n-chi Fibonachchi sonini memoizatsiya bilan hisoblaydi."""
    if n in xotira:
        return xotira[n]
    if n <= 1:
        return n
    xotira[n] = fibonachchi(n - 1, xotira) + fibonachchi(n - 2, xotira)
    return xotira[n]


# ============================================================
# 3. IKKILIK DARAXTNI KESIB O'TISH (Binary Tree Traversal)
# ============================================================
class Tugun:
    """Ikkilik daraxt tuguni."""
    def __init__(self, qiymat, chap=None, ong=None):
        self.qiymat = qiymat
        self.chap = chap
        self.ong = ong


def oldindan_tartib(tugun):
    """Pre-order traversal: ildiz → chap → o'ng."""
    if tugun is None:
        return []
    return [tugun.qiymat] + oldindan_tartib(tugun.chap) + oldindan_tartib(tugun.ong)


def ichki_tartib(tugun):
    """In-order traversal: chap → ildiz → o'ng."""
    if tugun is None:
        return []
    return ichki_tartib(tugun.chap) + [tugun.qiymat] + ichki_tartib(tugun.ong)


def keyingi_tartib(tugun):
    """Post-order traversal: chap → o'ng → ildiz."""
    if tugun is None:
        return []
    return keyingi_tartib(tugun.chap) + keyingi_tartib(tugun.ong) + [tugun.qiymat]


# ============================================================
# 4. BOG'LANGAN RO'YXATNI TESKARI CHIQARISH
# ============================================================
class BoglanganTugun:
    def __init__(self, qiymat, keyingi=None):
        self.qiymat = qiymat
        self.keyingi = keyingi


def teskari_chiqarish(tugun):
    """Bog'langan ro'yxatni teskari tartibda chiqaradi (rekursiv)."""
    if tugun is None:
        return []
    return teskari_chiqarish(tugun.keyingi) + [tugun.qiymat]


# ============================================================
# 5. LUG'ATNI REKURSIV KESIB O'TISH
# ============================================================
def lugat_kesish(malumot, chuqurlik=0):
    """Ichma-ich lug'atni rekursiv kesib o'tadi."""
    natija = []
    if isinstance(malumot, dict):
        for kalit, qiymat in malumot.items():
            natija.append(("  " * chuqurlik) + f"{kalit}:")
            natija.extend(lugat_kesish(qiymat, chuqurlik + 1))
    elif isinstance(malumot, list):
        for element in malumot:
            natija.extend(lugat_kesish(element, chuqurlik))
    else:
        natija.append(("  " * chuqurlik) + str(malumot))
    return natija


if __name__ == "__main__":
    print("=" * 55)
    print("REKURSIV ALGORITMLAR")
    print("=" * 55)

    # 1. Faktorial
    print("\n1. FAKTORIAL:")
    for n in [0, 1, 5, 10, 15]:
        print(f"   {n}! = {faktorial(n)}")

    # 2. Fibonachchi
    print("\n2. FIBONACHCHI SONLARI:")
    fib_list = [fibonachchi(i) for i in range(15)]
    print(f"   Birinchi 15 ta: {fib_list}")

    # 3. Ikkilik daraxt
    print("\n3. IKKILIK DARAXTNI KESIB O'TISH:")
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    daraxt = Tugun(1,
        Tugun(2, Tugun(4), Tugun(5)),
        Tugun(3, None, Tugun(6))
    )
    print(f"   Pre-order:  {oldindan_tartib(daraxt)}")
    print(f"   In-order:   {ichki_tartib(daraxt)}")
    print(f"   Post-order: {keyingi_tartib(daraxt)}")

    # 4. Bog'langan ro'yxat
    print("\n4. BOG'LANGAN RO'YXAT (teskari):")
    royxat = BoglanganTugun(1, BoglanganTugun(2, BoglanganTugun(3, BoglanganTugun(4))))
    print(f"   Teskari: {teskari_chiqarish(royxat)}")

    # 5. Lug'at kesish
    print("\n5. LUG'ATNI REKURSIV KESIB O'TISH:")
    talaba = {
        "ism": "Ali",
        "yosh": 20,
        "fanlar": {
            "matematika": {"ball": 90, "kredit": 4},
            "fizika": {"ball": 85, "kredit": 3},
        },
        "qiziqishlari": ["dasturlash", "sport"],
    }
    for satr in lugat_kesish(talaba):
        print(f"   {satr}")
