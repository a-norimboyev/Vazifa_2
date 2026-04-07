"""3-vazifa: Deadlock muammosini ko'rsatish va uni hal qilish."""

import threading
import time


# ============================================================
# 1-QISM: Deadlock yuzaga kelishi
# ============================================================
def deadlock_namoyishi():
    """Deadlock muammosini ko'rsatadi (ikki oqim ikki qulfni teskari tartibda oladi)."""
    qulf_A = threading.Lock()
    qulf_B = threading.Lock()

    def oqim_1():
        print("[Oqim-1] A qulfni olmoqda...")
        qulf_A.acquire()
        print("[Oqim-1] A qulfni oldi.")
        time.sleep(0.5)  # Deadlock uchun vaqt bering

        print("[Oqim-1] B qulfni olmoqda...")
        muddatli = qulf_B.acquire(timeout=2)
        if muddatli:
            print("[Oqim-1] B qulfni oldi.")
            qulf_B.release()
        else:
            print("[Oqim-1] B qulfni ololmadi - DEADLOCK!")
        qulf_A.release()

    def oqim_2():
        print("[Oqim-2] B qulfni olmoqda...")
        qulf_B.acquire()
        print("[Oqim-2] B qulfni oldi.")
        time.sleep(0.5)

        print("[Oqim-2] A qulfni olmoqda...")
        muddatli = qulf_A.acquire(timeout=2)
        if muddatli:
            print("[Oqim-2] A qulfni oldi.")
            qulf_A.release()
        else:
            print("[Oqim-2] A qulfni ololmadi - DEADLOCK!")
        qulf_B.release()

    print("=" * 60)
    print("DEADLOCK NAMOYISHI (timeout bilan aniqlash)")
    print("=" * 60)

    t1 = threading.Thread(target=oqim_1, name="Oqim-1")
    t2 = threading.Thread(target=oqim_2, name="Oqim-2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Deadlock namoyishi tugadi.\n")


# ============================================================
# 2-QISM: Deadlock hal qilish — qulflarni tartibli olish
# ============================================================
def deadlock_yechimi_tartibli():
    """Deadlockni hal qilish: qulflarni doimo bir xil tartibda olish."""
    qulf_A = threading.Lock()
    qulf_B = threading.Lock()

    def xavfsiz_oqim(nom):
        # Har doim A → B tartibda oling
        print(f"[{nom}] A qulfni olmoqda...")
        with qulf_A:
            print(f"[{nom}] A qulfni oldi.")
            time.sleep(0.3)
            print(f"[{nom}] B qulfni olmoqda...")
            with qulf_B:
                print(f"[{nom}] B qulfni oldi. Ish bajarilmoqda...")
                time.sleep(0.2)
        print(f"[{nom}] Barcha qulflar bo'shatildi.")

    print("=" * 60)
    print("YECHIM 1: Qulflarni tartibli olish")
    print("=" * 60)

    t1 = threading.Thread(target=xavfsiz_oqim, args=("Oqim-1",))
    t2 = threading.Thread(target=xavfsiz_oqim, args=("Oqim-2",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Tartibli qulflash tugadi — deadlock yo'q!\n")


# ============================================================
# 3-QISM: Deadlock hal qilish — threading.Lock() + timeout
# ============================================================
def deadlock_yechimi_timeout():
    """Deadlockni timeout bilan aniqlash va qayta urinish."""
    qulf_A = threading.Lock()
    qulf_B = threading.Lock()

    def oqim_timeout(nom, birinchi_qulf, ikkinchi_qulf, b_nomi, i_nomi):
        for urinish in range(3):
            birinchi_qulf.acquire()
            print(f"[{nom}] {b_nomi} qulfni oldi (urinish {urinish+1})")
            time.sleep(0.1)

            if ikkinchi_qulf.acquire(timeout=0.5):
                print(f"[{nom}] {i_nomi} qulfni oldi. Ish bajarilmoqda...")
                time.sleep(0.1)
                ikkinchi_qulf.release()
                birinchi_qulf.release()
                print(f"[{nom}] Muvaffaqiyatli tugadi!")
                return
            else:
                print(f"[{nom}] {i_nomi} qulfni ololmadi, qayta urinish...")
                birinchi_qulf.release()
                time.sleep(0.1)

        print(f"[{nom}] 3 urinishdan keyin ham muvaffaqiyatsiz.")

    print("=" * 60)
    print("YECHIM 2: Timeout va qayta urinish")
    print("=" * 60)

    t1 = threading.Thread(target=oqim_timeout, args=("Oqim-1", qulf_A, qulf_B, "A", "B"))
    t2 = threading.Thread(target=oqim_timeout, args=("Oqim-2", qulf_B, qulf_A, "B", "A"))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Timeout yechimi tugadi.\n")


if __name__ == "__main__":
    deadlock_namoyishi()
    print()
    deadlock_yechimi_tartibli()
    print()
    deadlock_yechimi_timeout()
