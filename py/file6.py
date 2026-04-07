"""6-vazifa: asyncio yordamida asinxron veb-skreper."""

import asyncio
import time
import re
from urllib.request import urlopen, Request
from urllib.error import URLError
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor


class SarlavhaAjratuvchi(HTMLParser):
    """HTML dan sarlavha va matn ajratib oladi."""

    def __init__(self):
        super().__init__()
        self.sarlavhalar = []
        self.joriy_teg = None
        self.title = ""
        self._title_ichida = False

    def handle_starttag(self, tag, attrs):
        if tag in ("h1", "h2", "h3"):
            self.joriy_teg = tag
        if tag == "title":
            self._title_ichida = True

    def handle_endtag(self, tag):
        if tag in ("h1", "h2", "h3"):
            self.joriy_teg = None
        if tag == "title":
            self._title_ichida = False

    def handle_data(self, data):
        if self._title_ichida:
            self.title += data.strip()
        if self.joriy_teg:
            matn = data.strip()
            if matn:
                self.sarlavhalar.append((self.joriy_teg, matn))


def sahifani_yukla(url):
    """Bitta sahifani sinxron yuklab oladi (threadda ishlatiladi)."""
    headers = {"User-Agent": "Mozilla/5.0 (Educational Bot)"}
    req = Request(url, headers=headers)
    with urlopen(req, timeout=10) as javob:
        return javob.read().decode("utf-8", errors="replace")


def kontentni_qayta_ishla(html, url):
    """HTML kontentni tahlil qiladi."""
    parser = SarlavhaAjratuvchi()
    parser.feed(html)

    # So'zlar sonini hisoblash (teglarni olib tashlab)
    toza_matn = re.sub(r"<[^>]+>", " ", html)
    sozlar = len(toza_matn.split())

    return {
        "url": url,
        "title": parser.title,
        "sarlavhalar_soni": len(parser.sarlavhalar),
        "sarlavhalar": parser.sarlavhalar[:5],
        "sozlar_soni": sozlar,
        "html_hajmi": len(html),
    }


async def sahifani_asinxron_yukla(url, executor):
    """Sahifani asinxron yuklab oladi va qayta ishlaydi."""
    loop = asyncio.get_event_loop()
    try:
        boshi = time.perf_counter()
        html = await loop.run_in_executor(executor, sahifani_yukla, url)
        yuklash_vaqti = time.perf_counter() - boshi

        natija = kontentni_qayta_ishla(html, url)
        natija["yuklash_vaqti"] = yuklash_vaqti
        natija["holat"] = "muvaffaqiyatli"
        return natija
    except (URLError, Exception) as e:
        return {
            "url": url,
            "holat": "xato",
            "xabar": str(e),
        }


async def asosiy():
    """Bir nechta sahifalarni bir vaqtda yuklab oladi."""
    sahifalar = [
        "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "https://en.wikipedia.org/wiki/Asyncio",
        "https://en.wikipedia.org/wiki/Web_scraping",
        "https://en.wikipedia.org/wiki/Concurrency_(computer_science)",
        "https://en.wikipedia.org/wiki/Parallel_computing",
    ]

    print("=" * 60)
    print("ASINXRON VEB-SKREPER (asyncio)")
    print("=" * 60)
    print(f"Jami {len(sahifalar)} ta sahifa yuklanadi...\n")

    boshi = time.perf_counter()

    executor = ThreadPoolExecutor(max_workers=5)
    vazifalar = [sahifani_asinxron_yukla(url, executor) for url in sahifalar]
    natijalar = await asyncio.gather(*vazifalar)

    umumiy_vaqt = time.perf_counter() - boshi

    print("-" * 60)
    for natija in natijalar:
        if natija["holat"] == "muvaffaqiyatli":
            print(f"✓ {natija['title'][:50]}")
            print(f"  URL: {natija['url']}")
            print(f"  So'zlar: {natija['sozlar_soni']:,}, HTML: {natija['html_hajmi']:,} bayt")
            print(f"  Sarlavhalar: {natija['sarlavhalar_soni']} ta")
            print(f"  Yuklash vaqti: {natija['yuklash_vaqti']:.2f} s")
        else:
            print(f"✗ {natija['url']}")
            print(f"  Xato: {natija['xabar']}")
        print()

    print("=" * 60)
    print(f"Umumiy vaqt: {umumiy_vaqt:.2f} s")
    muvaffaqiyatli = sum(1 for n in natijalar if n["holat"] == "muvaffaqiyatli")
    print(f"Muvaffaqiyatli: {muvaffaqiyatli}/{len(sahifalar)}")
    executor.shutdown(wait=False)


if __name__ == "__main__":
    asyncio.run(asosiy())
