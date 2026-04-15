"""15-vazifa: Ichma-ich ro'yxatni tekislash (Flatten nested list)."""


# ============================================================
# 1. REKURSIV TEKISLASH (asosiy usul)
# ============================================================
def tekisla(royxat):
    """Ichma-ich ro'yxatni rekursiv tekislaydi.

    Misol: [1, [2, [3, 4], 5]] → [1, 2, 3, 4, 5]
    """
    natija = []
    for element in royxat:
        if isinstance(element, list):
            natija.extend(tekisla(element))
        else:
            natija.append(element)
    return natija


# ============================================================
# 2. GENERATOR BILAN TEKISLASH (xotira tejamkor)
# ============================================================
def tekisla_generator(royxat):
    """Generator yordamida tekislaydi (lazy evaluation)."""
    for element in royxat:
        if isinstance(element, list):
            yield from tekisla_generator(element)
        else:
            yield element


# ============================================================
# 3. CHUQURLIK BILAN TEKISLASH (ma'lum chuqurlikkachagina)
# ============================================================
def tekisla_chuqurlik(royxat, max_chuqurlik=1):
    """Faqat berilgan chuqurlikkacha tekislaydi.

    Misol (chuqurlik=1): [1, [2, [3, 4]]] → [1, 2, [3, 4]]
    """
    natija = []
    for element in royxat:
        if isinstance(element, list) and max_chuqurlik > 0:
            natija.extend(tekisla_chuqurlik(element, max_chuqurlik - 1))
        else:
            natija.append(element)
    return natija


# ============================================================
# 4. ITERATIV TEKISLASH (stack yordamida)
# ============================================================
def tekisla_iterativ(royxat):
    """Stack yordamida iterativ tekislaydi."""
    stack = list(royxat[::-1])  # Teskari tartibda stackga joylash
    natija = []
    while stack:
        element = stack.pop()
        if isinstance(element, list):
            # Ichki elementlarni teskari tartibda stackga qo'shish
            for i in range(len(element) - 1, -1, -1):
                stack.append(element[i])
        else:
            natija.append(element)
    return natija


if __name__ == "__main__":
    print("=" * 55)
    print("ICHMA-ICH RO'YXATNI TEKISLASH")
    print("=" * 55)

    # Test ma'lumotlari
    testlar = [
        [1, [2, [3, 4], 5]],
        [[1, 2], [3, [4, [5, 6]]], 7],
        [[], [1], [[2]], [[[3]]]],
        [1, 2, 3],  # Allaqachon tekis
        [[[[["chuqur"]]]]],
        ["a", ["b", ["c", "d"]], "e"],
    ]

    # 1. Rekursiv tekislash
    print("\n1. REKURSIV TEKISLASH:")
    for test in testlar:
        print(f"   {test}")
        print(f"   → {tekisla(test)}")
        print()

    # 2. Generator bilan
    print("2. GENERATOR BILAN:")
    misol = [1, [2, [3, 4], 5]]
    print(f"   {misol} → {list(tekisla_generator(misol))}")

    # 3. Chuqurlik bilan
    print("\n3. CHUQURLIK BILAN TEKISLASH:")
    misol = [1, [2, [3, [4, [5]]]]]
    for chuq in range(4):
        print(f"   chuqurlik={chuq}: {tekisla_chuqurlik(misol, chuq)}")

    # 4. Iterativ
    print("\n4. ITERATIV TEKISLASH:")
    for test in testlar:
        rek = tekisla(test)
        itr = tekisla_iterativ(test)
        moslik = "✓" if rek == itr else "✗"
        print(f"   {moslik} {test} → {itr}")

    # Samaradorlik solishtirish
    print("\n" + "=" * 55)
    print("TEKSHIRISH: Barcha usullar bir xil natija beradi:")
    import time
    katta_royxat = list(range(100))
    # Ichma-ich qilish
    for _ in range(5):
        katta_royxat = [katta_royxat[:50], katta_royxat[50:]]

    boshi = time.perf_counter()
    n1 = tekisla(katta_royxat)
    rek_vaqt = time.perf_counter() - boshi

    boshi = time.perf_counter()
    n2 = list(tekisla_generator(katta_royxat))
    gen_vaqt = time.perf_counter() - boshi

    boshi = time.perf_counter()
    n3 = tekisla_iterativ(katta_royxat)
    itr_vaqt = time.perf_counter() - boshi

    print(f"  Rekursiv:  {len(n1)} element, {rek_vaqt:.6f} s")
    print(f"  Generator: {len(n2)} element, {gen_vaqt:.6f} s")
    print(f"  Iterativ:  {len(n3)} element, {itr_vaqt:.6f} s")
    print(f"  Natijalar mos: {n1 == n2 == n3}")
