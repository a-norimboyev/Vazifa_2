"""2-vazifa: Ko'p oqimli fayl yuklash (multithreading) va thread-safe navbat."""

import threading
import queue
import time
import urllib.request
import os


def faylni_yukla(url, saqlash_papkasi, natija_navbat):
    """Bitta faylni internetdan yuklab oladi."""
    oqim_nomi = threading.current_thread().name
    fayl_nomi = url.split("/")[-1] or "index.html"
    fayl_yoli = os.path.join(saqlash_papkasi, fayl_nomi)

    try:
        print(f"[{oqim_nomi}] Yuklanmoqda: {url}")
        boshlanish = time.perf_counter()
        urllib.request.urlretrieve(url, fayl_yoli)
        vaqt = time.perf_counter() - boshlanish
        hajm = os.path.getsize(fayl_yoli)
        natija_navbat.put({
            "url": url,
            "fayl": fayl_nomi,
            "hajm": hajm,
            "vaqt": vaqt,
            "holat": "muvaffaqiyatli",
            "oqim": oqim_nomi,
        })
        print(f"[{oqim_nomi}] Tugadi: {fayl_nomi} ({hajm} bayt, {vaqt:.2f} s)")
    except Exception as e:
        natija_navbat.put({
            "url": url,
            "holat": "xato",
            "xabar": str(e),
            "oqim": oqim_nomi,
        })
        print(f"[{oqim_nomi}] Xato: {url} - {e}")


def ishchi_oqim(vazifa_navbat, saqlash_papkasi, natija_navbat):
    """Navbatdan vazifalarni olib, yuklab oladi."""
    while True:
        try:
            url = vazifa_navbat.get(timeout=1)
        except queue.Empty:
            break
        faylni_yukla(url, saqlash_papkasi, natija_navbat)
        vazifa_navbat.task_done()


if __name__ == "__main__":
    # Yuklab olish uchun URL ro'yxati (ochiq test fayllari)
    urllar = [
        "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "https://filesamples.com/samples/document/txt/sample1.txt",
        "https://filesamples.com/samples/document/txt/sample2.txt",
        "https://filesamples.com/samples/document/txt/sample3.txt",
        "https://www.w3.org/TR/PNG/iso_8859-1.txt",
    ]

    SAQLASH_PAPKASI = "yuklangan_fayllar"
    OQIMLAR_SONI = 3

    os.makedirs(SAQLASH_PAPKASI, exist_ok=True)

    # Thread-safe navbatlar
    vazifa_navbat = queue.Queue()
    natija_navbat = queue.Queue()

    for url in urllar:
        vazifa_navbat.put(url)

    # Oqimlarni yaratish va ishga tushirish
    oqimlar = []
    boshlanish = time.perf_counter()

    for i in range(OQIMLAR_SONI):
        t = threading.Thread(
            target=ishchi_oqim,
            args=(vazifa_navbat, SAQLASH_PAPKASI, natija_navbat),
            name=f"Oqim-{i+1}",
        )
        oqimlar.append(t)
        t.start()

    # Barcha oqimlar tugashini kutish
    for t in oqimlar:
        t.join()

    umumiy_vaqt = time.perf_counter() - boshlanish

    # Natijalarni chiqarish
    print("\n" + "=" * 60)
    print("NATIJALAR:")
    print("=" * 60)
    muvaffaqiyatli = 0
    xatolar = 0
    while not natija_navbat.empty():
        natija = natija_navbat.get()
        if natija["holat"] == "muvaffaqiyatli":
            muvaffaqiyatli += 1
        else:
            xatolar += 1

    print(f"Jami URL: {len(urllar)}")
    print(f"Muvaffaqiyatli: {muvaffaqiyatli}")
    print(f"Xatolar: {xatolar}")
    print(f"Oqimlar soni: {OQIMLAR_SONI}")
    print(f"Umumiy vaqt: {umumiy_vaqt:.2f} s")
