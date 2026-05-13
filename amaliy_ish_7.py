from __future__ import annotations

import re
from abc import ABC, abstractmethod

try:
    import pandas as pd
except ImportError:  # pragma: no cover - environment dependent
    pd = None


def filter_products(products: list[dict]) -> list[dict]:
    return list(filter(lambda product: product["price"] > 100 and product["in_stock"], products))


def transform_usernames(usernames: list[str]) -> list[str]:
    return list(map(lambda username: f"ID-{username.upper()}", usernames))


divisible_squares = [number**2 for number in range(1, 101) if number % 3 == 0 and number % 5 == 0]


def average_salary_by_city():
    if pd is None:
        return "Pandas o'rnatilmagan, groupby namunasi bajarilmadi."

    df = pd.DataFrame(
        {
            "city": ["Toshkent", "Samarqand", "Toshkent", "Buxoro", "Samarqand"],
            "salary": [7000, 5500, 9000, 6000, 6500],
        }
    )
    return df.groupby("city")["salary"].mean()


def extract_phone_numbers(text: str) -> list[str]:
    pattern = r"\+998\d{9}"
    return re.findall(pattern, text)


def fibonacci(number: int) -> int:
    if number < 0:
        raise ValueError("n manfiy bo'lmasligi kerak")
    if number in (0, 1):
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


def logger(function):
    def wrapper(*args, **kwargs):
        print("Log: Funksiya chaqirildi")
        return function(*args, **kwargs)

    return wrapper


@logger
def greet_reader(name: str) -> str:
    return f"Assalomu alaykum, {name}!"


def sort_students(students: list[dict]) -> list[dict]:
    return sorted(students, key=lambda student: (-student["grade"], student["name"]))


def discounted_prices(prices: dict[str, float]) -> dict[str, float]:
    return {name: value * 0.9 for name, value in prices.items() if value > 0}


def constraint_solutions() -> list[tuple[int, int]]:
    return [(a_value, b_value) for a_value in range(11) for b_value in range(11) if a_value + b_value == 10 and a_value > 5]


class LibraryBase(ABC):
    @abstractmethod
    def calculate_limit(self) -> int:
        raise NotImplementedError


class Item:
    def __init__(self, title: str) -> None:
        self.title = title
        self.is_available = True

    def get_fine_rate(self) -> int:
        raise NotImplementedError

    def display_info(self) -> str:
        status = "Mavjud" if self.is_available else "Band"
        return f"Nomi: {self.title} | Holati: {status}"


class Book(Item):
    def __init__(self, title: str, author: str, isbn: str, is_available: bool = True) -> None:
        super().__init__(title)
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def display_info(self) -> str:
        status = "Mavjud" if self.is_available else "Band"
        return f"Kitob: {self.title} | Muallif: {self.author} | ISBN: {self.isbn} | Holati: {status}"

    def get_fine_rate(self) -> int:
        return 2000


class Magazine(Item):
    def __init__(self, title: str, issue_number: int, is_available: bool = True) -> None:
        super().__init__(title)
        self.issue_number = issue_number
        self.is_available = is_available

    def display_info(self) -> str:
        status = "Mavjud" if self.is_available else "Band"
        return f"Jurnal: {self.title} | Nashr soni: {self.issue_number} | Holati: {status}"

    def get_fine_rate(self) -> int:
        return 5000


class Member:
    def __init__(self, name: str, member_id: str) -> None:
        self.name = name
        self.__member_id = member_id

    def get_id(self) -> str:
        return self.__member_id


class StudentLibrary(LibraryBase):
    def calculate_limit(self) -> int:
        return 3


class StaffLibrary(LibraryBase):
    def calculate_limit(self) -> int:
        return 7


class SmartLibrary:
    def __init__(self) -> None:
        self.items: list[Item] = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def borrow_item(self, title: str) -> Item | None:
        item = next((entry for entry in self.items if entry.title.lower() == title.lower() and entry.is_available), None)
        if item is not None:
            item.is_available = False
        return item

    def search_by_title(self, keyword: str) -> list[Item]:
        return list(filter(lambda item: keyword.lower() in item.title.lower(), self.items))

    def available_items(self) -> list[Item]:
        return list(filter(lambda item: item.is_available, self.items))

    def total_fine_rate(self) -> int:
        return sum(item.get_fine_rate() for item in self.available_items())


def print_section(title: str) -> None:
    print(f"\n{'=' * 12} {title} {'=' * 12}")


def run_declarative_examples() -> None:
    print_section("13-mavzu: Deklarativ dasturlash")

    products = [
        {"name": "A", "price": 120, "in_stock": True},
        {"name": "B", "price": 80, "in_stock": True},
        {"name": "C", "price": 180, "in_stock": False},
        {"name": "D", "price": 250, "in_stock": True},
    ]
    print("1. Filter:", filter_products(products))

    usernames = ["aziz", "dilnoza", "javohir"]
    print("2. Map:", transform_usernames(usernames))

    print("3. List comprehension:", divisible_squares)
    print("4. Pandas groupby:\n", average_salary_by_city())

    text = "Bog'lanish uchun +998901234567 yoki +998991112233 raqamlariga qo'ng'iroq qiling."
    print("5. RegEx:", extract_phone_numbers(text))

    print("6. Fibonacci f(8):", fibonacci(8))
    print("7. Dekorator:", greet_reader("Azizjon"))

    students = [
        {"name": "Zarina", "grade": 89},
        {"name": "Ali", "grade": 95},
        {"name": "Anvar", "grade": 95},
        {"name": "Malika", "grade": 72},
    ]
    print("8. Sorting:", sort_students(students))

    prices = {"kitob": 50000, "daftar": 12000, "qalam": 5000}
    print("9. Dict comprehension:", discounted_prices(prices))
    print("10. Constraintlar:", constraint_solutions())


def run_oop_library_demo() -> None:
    print_section("14-mavzu: Aqlli Kutubxona")

    library = SmartLibrary()
    member = Member("Azizjon", "M-001")
    student_section = StudentLibrary()
    staff_section = StaffLibrary()

    items = [
        Book("Python Asoslari", "A. Valiyev", "ISBN-001"),
        Book("Sun'iy Intellekt", "B. Karimov", "ISBN-002"),
        Book("Algoritmlar", "D. Xasanov", "ISBN-003"),
        Magazine("Tech Today", 12),
        Magazine("Science World", 7),
    ]

    for item in items:
        library.add_item(item)

    borrowed_item = library.borrow_item("Python Asoslari")
    search_result = library.search_by_title("sun")
    available_items = library.available_items()

    print("A'zo ID:", member.get_id())
    print("Student limit:", student_section.calculate_limit())
    print("Staff limit:", staff_section.calculate_limit())
    print("Berilgan element:", borrowed_item.display_info() if borrowed_item else "Topilmadi")
    print("Qidiruv natijalari:")
    for item in search_result:
        print(item.display_info())

    print("Mavjud elementlar:")
    for item in available_items:
        print(item.display_info())
    print("Umumiy jarima stavkasi:", library.total_fine_rate(), "so'm")


if __name__ == "__main__":
    run_declarative_examples()
    run_oop_library_demo()