"""
7-amaliy topshiriq, 1-mavzu:
Ma'lumotlarni filtrlash (Functional Approach)

Talab:
Narxi 100 dan yuqori va omborda mavjud mahsulotlarni
filter() funksiyasi orqali ajratib olish.
"""


def parse_in_stock(value: str) -> bool:
    normalized = value.strip().lower()
    return normalized in ("ha", "h", "yes", "y", "true", "1")


def read_products() -> list[dict]:
    products = []

    count = int(input("Nechta mahsulot kiritasiz? "))

    i = 1
    while i <= count:
        print(f"\n{i}-mahsulot:")
        name = input("Nomi: ").strip()
        price = float(input("Narxi: ").strip())
        in_stock = parse_in_stock(input("Omborda bormi? (ha/yo'q): "))

        products.append({"name": name, "price": price, "in_stock": in_stock})
        i += 1

    return products


products = read_products()

# Narxi > 100 va in_stock=True bo'lgan mahsulotlar
filtered_products = list(filter(lambda p: p["price"] > 100 and p["in_stock"], products))

print("\nFiltrlangan mahsulotlar:")
if filtered_products:
    formatted = map(
        lambda product: f"- {product['name']}: price={product['price']}, in_stock={product['in_stock']}",
        filtered_products,
    )
    print("\n".join(formatted))
else:
    print("Mos mahsulot topilmadi.")
