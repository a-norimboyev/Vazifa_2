"""9-vazifa: Producer-Consumer tizimi ustuvor (prioritetli) navbat bilan."""

import threading
import queue
import time
import random


# Ustuvorlik nomlari
USTUVORLIK_NOMLARI = {1: "YUQORI", 2: "O'RTA", 3: "PAST"}


class Vazifa:
    """Ustuvorlikka ega vazifa."""

    _counter = 0
    _lock = threading.Lock()

    def __init__(self, ustuvorlik, nomi, malumot, tugash=False):
        self.ustuvorlik = ustuvorlik  # 1=yuqori, 2=o'rta, 3=past
        self.nomi = nomi
        self.malumot = malumot
        self.tugash = tugash
        self.yaratilgan_vaqt = time.perf_counter()

        # PriorityQueue uchun tartib raqami (bir xil ustuvorlikda FIFO)
        with Vazifa._lock:
            Vazifa._counter += 1
            self._tartib = Vazifa._counter

    def __lt__(self, boshqa):
        """PriorityQueue uchun solishtirish."""
        # Tugash signallari doimo oxirgi
        if self.tugash != boshqa.tugash:
            return not self.tugash
        if self.ustuvorlik == boshqa.ustuvorlik:
            return self._tartib < boshqa._tartib
        return self.ustuvorlik < boshqa.ustuvorlik

    def __repr__(self):
        if self.tugash:
            return "Vazifa(TUGASH)"
        return f"Vazifa({USTUVORLIK_NOMLARI[self.ustuvorlik]}, '{self.nomi}')"


def tugash_signali():
    """PriorityQueue uchun mos tugash signali yaratadi."""
    return Vazifa(ustuvorlik=999, nomi="TUGASH", malumot="", tugash=True)


def ishlab_chiqaruvchi(producer_id, navbat, vazifalar_soni, stop_event):
    """Turli ustuvorlikdagi vazifalarni yaratadi."""
    nom = f"Producer-{producer_id}"

    for i in range(vazifalar_soni):
        if stop_event.is_set():
            break

        ustuvorlik = random.choice([1, 2, 3])
        vazifa = Vazifa(
            ustuvorlik=ustuvorlik,
            nomi=f"{nom}_vazifa_{i+1}",
            malumot=f"Ma'lumot #{random.randint(100, 999)}",
        )
        navbat.put(vazifa)
        print(
            f"  [{nom}] Yaratdi: {vazifa.nomi} "
            f"(ustuvorlik: {USTUVORLIK_NOMLARI[ustuvorlik]})"
        )
        time.sleep(random.uniform(0.05, 0.2))

    print(f"  [{nom}] Barcha vazifalar yaratildi.")


def istehmolchi(consumer_id, navbat, bajarilgan, stop_event):
    """Navbatdan vazifalarni ustuvorlik tartibida oladi va qayta ishlaydi."""
    nom = f"Consumer-{consumer_id}"
    ishlov_soni = 0

    while not stop_event.is_set():
        try:
            vazifa = navbat.get(timeout=1)
        except queue.Empty:
            continue

        if vazifa.tugash:
            navbat.task_done()
            break

        # Vazifani qayta ishlash
        kutish = time.perf_counter() - vazifa.yaratilgan_vaqt
        print(
            f"  [{nom}] Ishlayapti: {vazifa.nomi} "
            f"({USTUVORLIK_NOMLARI[vazifa.ustuvorlik]}, "
            f"kutish: {kutish:.3f}s)"
        )
        time.sleep(random.uniform(0.1, 0.3))  # Ishlov berish simulyatsiyasi

        bajarilgan.append({
            "vazifa": vazifa.nomi,
            "ustuvorlik": vazifa.ustuvorlik,
            "consumer": nom,
            "kutish_vaqti": kutish,
        })
        ishlov_soni += 1
        navbat.task_done()

    print(f"  [{nom}] Tugadi ({ishlov_soni} ta vazifa bajarildi).")


if __name__ == "__main__":
    PRODUCERLAR_SONI = 3
    CONSUMERLAR_SONI = 2
    HAR_PRODUCER_VAZIFALAR = 5

    navbat = queue.PriorityQueue()
    bajarilgan = []  # Natijalar
    stop_event = threading.Event()

    print("=" * 65)
    print("PRODUCER-CONSUMER TIZIMI (Ustuvor navbat bilan)")
    print("=" * 65)
    print(f"Producerlar: {PRODUCERLAR_SONI}, Consumerlar: {CONSUMERLAR_SONI}")
    print(f"Har bir producer {HAR_PRODUCER_VAZIFALAR} ta vazifa yaratadi.")
    print()

    boshi = time.perf_counter()

    # Producerlarni yaratish
    producer_oqimlari = []
    for i in range(PRODUCERLAR_SONI):
        t = threading.Thread(
            target=ishlab_chiqaruvchi,
            args=(i + 1, navbat, HAR_PRODUCER_VAZIFALAR, stop_event),
        )
        producer_oqimlari.append(t)

    # Consumerlarni yaratish
    consumer_oqimlari = []
    for i in range(CONSUMERLAR_SONI):
        t = threading.Thread(
            target=istehmolchi,
            args=(i + 1, navbat, bajarilgan, stop_event),
        )
        consumer_oqimlari.append(t)

    # Barcha oqimlarni ishga tushirish
    for t in consumer_oqimlari:
        t.start()
    for t in producer_oqimlari:
        t.start()

    # Producerlar tugashini kutish
    for t in producer_oqimlari:
        t.join()

    # Consumerlarni to'xtatish uchun tugash signallari
    for _ in range(CONSUMERLAR_SONI):
        navbat.put(tugash_signali())

    for t in consumer_oqimlari:
        t.join()

    umumiy_vaqt = time.perf_counter() - boshi

    # Natijalar statistikasi
    print("\n" + "=" * 65)
    print("NATIJALAR:")
    print("=" * 65)

    ustuvorlik_soni = {1: 0, 2: 0, 3: 0}
    for b in bajarilgan:
        ustuvorlik_soni[b["ustuvorlik"]] += 1

    print(f"Jami bajarilgan vazifalar: {len(bajarilgan)}")
    for ust, soni in sorted(ustuvorlik_soni.items()):
        print(f"  {USTUVORLIK_NOMLARI[ust]}: {soni} ta")

    if bajarilgan:
        ortacha_kutish = sum(b["kutish_vaqti"] for b in bajarilgan) / len(bajarilgan)
        print(f"O'rtacha kutish vaqti: {ortacha_kutish:.3f} s")

    print(f"Umumiy vaqt: {umumiy_vaqt:.2f} s")
