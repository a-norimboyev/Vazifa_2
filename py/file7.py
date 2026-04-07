"""7-vazifa: Pipeline (konveyer) pattern — o'qish → qayta ishlash → yozish."""

import threading
import queue
import time
import random
import os


# Signal uchun maxsus qiymat (sentinel)
TUGASH_SIGNALI = None


def oqish_bosqichi(chiqish_navbat, ma_lumotlar):
    """1-bosqich: Ma'lumotlarni o'qib, navbatga qo'yadi."""
    oqim_nomi = threading.current_thread().name
    for i, element in enumerate(ma_lumotlar):
        print(f"[{oqim_nomi}] O'qildi: element #{i+1}")
        chiqish_navbat.put({"indeks": i, "xom_malumot": element})
        time.sleep(0.1)  # O'qish simulyatsiyasi

    chiqish_navbat.put(TUGASH_SIGNALI)
    print(f"[{oqim_nomi}] O'qish tugadi.")


def qayta_ishlash_bosqichi(kirish_navbat, chiqish_navbat):
    """2-bosqich: Ma'lumotlarni qayta ishlab, keyingi bosqichga uzatadi."""
    oqim_nomi = threading.current_thread().name
    ishlov_soni = 0

    while True:
        element = kirish_navbat.get()
        if element is TUGASH_SIGNALI:
            chiqish_navbat.put(TUGASH_SIGNALI)
            kirish_navbat.task_done()
            break

        # Qayta ishlash: matnni katta harfga, raqamlarni kvadratga
        xom = element["xom_malumot"]
        if isinstance(xom, str):
            ishlangan = xom.upper()
        elif isinstance(xom, (int, float)):
            ishlangan = xom ** 2
        else:
            ishlangan = str(xom)

        element["ishlangan_malumot"] = ishlangan
        ishlov_soni += 1
        print(f"[{oqim_nomi}] Ishlandi #{element['indeks']+1}: {xom} → {ishlangan}")
        chiqish_navbat.put(element)
        kirish_navbat.task_done()
        time.sleep(0.15)  # Qayta ishlash simulyatsiyasi

    print(f"[{oqim_nomi}] Qayta ishlash tugadi ({ishlov_soni} ta element).")


def yozish_bosqichi(kirish_navbat, fayl_yoli):
    """3-bosqich: Qayta ishlangan ma'lumotlarni faylga yozadi."""
    oqim_nomi = threading.current_thread().name
    yozilgan_soni = 0

    with open(fayl_yoli, "w", encoding="utf-8") as fayl:
        fayl.write("Indeks | Xom ma'lumot | Ishlangan ma'lumot\n")
        fayl.write("-" * 50 + "\n")

        while True:
            element = kirish_navbat.get()
            if element is TUGASH_SIGNALI:
                kirish_navbat.task_done()
                break

            satr = (
                f"{element['indeks']+1:>5} | "
                f"{str(element['xom_malumot']):>15} | "
                f"{str(element['ishlangan_malumot']):>20}\n"
            )
            fayl.write(satr)
            yozilgan_soni += 1
            print(f"[{oqim_nomi}] Yozildi #{element['indeks']+1}")
            kirish_navbat.task_done()
            time.sleep(0.05)  # Yozish simulyatsiyasi

    print(f"[{oqim_nomi}] Yozish tugadi ({yozilgan_soni} ta element). Fayl: {fayl_yoli}")


if __name__ == "__main__":
    # Test ma'lumotlari
    ma_lumotlar = [
        "salom", 5, "dunyo", 12, "python", 7,
        "pipeline", 25, "oqim", 3, "test", 100,
    ]

    CHIQISH_FAYLI = "pipeline_natija.txt"

    # Navbatlar — bosqichlar orasidagi bufer
    navbat_1 = queue.Queue(maxsize=5)  # o'qish → qayta ishlash
    navbat_2 = queue.Queue(maxsize=5)  # qayta ishlash → yozish

    print("=" * 60)
    print("PIPELINE PATTERN: O'qish → Qayta ishlash → Yozish")
    print("=" * 60)
    print(f"Jami elementlar: {len(ma_lumotlar)}\n")

    boshi = time.perf_counter()

    # 3 ta bosqich — har biri alohida oqimda
    oqish_oqimi = threading.Thread(
        target=oqish_bosqichi, args=(navbat_1, ma_lumotlar), name="O'qish"
    )
    ishlash_oqimi = threading.Thread(
        target=qayta_ishlash_bosqichi, args=(navbat_1, navbat_2), name="Ishlash"
    )
    yozish_oqimi = threading.Thread(
        target=yozish_bosqichi, args=(navbat_2, CHIQISH_FAYLI), name="Yozish"
    )

    oqish_oqimi.start()
    ishlash_oqimi.start()
    yozish_oqimi.start()

    oqish_oqimi.join()
    ishlash_oqimi.join()
    yozish_oqimi.join()

    umumiy_vaqt = time.perf_counter() - boshi

    print(f"\nPipeline tugadi. Umumiy vaqt: {umumiy_vaqt:.2f} s")

    # Natijani ko'rsatish
    if os.path.exists(CHIQISH_FAYLI):
        print(f"\n{CHIQISH_FAYLI} mazmuni:")
        print("-" * 50)
        with open(CHIQISH_FAYLI, encoding="utf-8") as f:
            print(f.read())
