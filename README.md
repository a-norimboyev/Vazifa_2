# 📩 Contact Form orqali xabarlarni saqlash va ko‘rsatish (Django)

Ushbu Django veb-ilovasi foydalanuvchilar tomonidan yuborilgan xabarlarni qabul qiladi, maʼlumotlar bazasiga xavfsiz saqlaydi hamda ularni `/xabarlar` sahifasida qulay va chiroyli jadval ko‘rinishida aks ettiradi.

---

## 🌟 Asosiy imkoniyatlar

1. **Bosh sahifa (`http://127.0.0.1:8000/`)**:
   - Chiroyli va zamonaviy Bootstrap 5 dizaynidagi kontakt formasi.
   - Maydonlar:
     - **Ism** (First Name)
     - **Familiya** (Last Name)
     - **Telefon raqam** (Phone Number)
     - **Email manzil** (Email)
     - **Yuborilgan xabar** (Message)
     - **[Jo‘natish]** tugmasi
   - To‘liq validatsiya va CSRF himoyasi.

2. **Xabarlarni saqlash va qayta yo‘naltirish (Redirect)**:
   - Foydalanuvchi "Jo‘natish" tugmasini bosganda, maʼlumotlar `POST` so‘rovi orqali yuboriladi.
   - Maʼlumotlar bazasiga saqlanadi.
   - Foydalanuvchi avtomatik tarzda `http://127.0.0.1:8000/xabarlar` sahifasiga yo‘naltiriladi (`HTTP 302 Redirect`).

3. **Xabarlar jadvali sahifasi (`http://127.0.0.1:8000/xabarlar`)**:
   - Barcha foydalanuvchilardan kelgan xabarlar tartibli jadvalda ko‘rsatiladi.
   - Jadval ustunlari:
     - **№** (Tartib raqami)
     - **Ism**
     - **Familiya**
     - **Telefon raqam** (bosilganda qo‘ng‘iroq qilish imkoniyati bilan)
     - **Email** (bosilganda xat yozish `mailto:` havolasi bilan)
     - **Yuborilgan xabar**

---

## 📁 Loyiha Strukturasi

```text
Vazifa_2-main/
│
├── config/                  # Asosiy Django loyiha sozlamalari
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # App va Template konfiguratsiyasi
│   ├── urls.py             # Asosiy URL yo'naltiruvchi
│   └── wsgi.py
│
├── contacts/                # Kontakt va xabarlar ilovasi
│   ├── migrations/         # Ma'lumotlar bazasi migratsiyalari
│   ├── __init__.py
│   ├── admin.py            # Django Admin konfiguratsiyasi
│   ├── apps.py
│   ├── forms.py            # ContactMessageForm (ModelForm)
│   ├── models.py           # ContactMessage modeli
│   ├── tests.py            # Avtomatlashtirilgan testlar
│   ├── urls.py             # contacts ilovasi URLlari
│   └── views.py            # contact_view va messages_list_view
│
├── templates/               # HTML shablonlar
│   ├── base.html           # Asosiy shablon (Bootstrap 5, Navbar, Footer)
│   └── contacts/
│       ├── contact_form.html   # Bosh sahifa formasi
│       └── messages_list.html  # Xabarlar jadvali
│
├── manage.py                # Django boshqaruv skripti
├── db.sqlite3               # SQLite ma'lumotlar bazasi
├── .gitignore               # Git e'tibordan chetda qoldiradigan fayllar
└── README.md                # Loyiha qo'llanmasi
```

---

## 🚀 Loyihani o‘rnatish va ishga tushirish

### 1. Loyihani yuklab olish yoki klonlash:
```bash
git clone <repository_url>
cd Vazifa_2-main
```

### 2. Virtual muhitni faollashtirish (ixtiyoriy, lekin tavsiya etiladi):
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 3. Django o‘rnatilganligini tekshirish:
```bash
pip install django
```

### 4. Migratsiyalarni amalga oshirish:
```bash
python manage.py migrate
```

### 5. Serverni ishga tushirish:
```bash
python manage.py runserver
```

Brauzerda quyidagi manzillarni oching:
- Forma: **http://127.0.0.1:8000/**
- Xabarlar jadvali: **http://127.0.0.1:8000/xabarlar**
- Admin panel: **http://127.0.0.1:8000/admin/**

---

## 🧪 Avtomatlashtirilgan Testlarni Tekshirish

Loyiha to‘liq unit testlar bilan qoplangan. Testlarni ishga tushirish uchun:

```bash
python manage.py test
```

Natija:
```text
Found 4 test(s).
Creating test database for alias 'default'...
....
----------------------------------------------------------------------
Ran 4 tests in 0.294s

OK
```
