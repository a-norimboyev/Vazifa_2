import math

# 1. Ma'lumotlarni qayta ishlash funksiyasi (Hisoblash mantiqi)
def calculate_area(shape, data):
    if shape == "doira":
        r = data[0]
        return math.pi * (r ** 2) # S = πr²
    elif shape == "to'rtburchak":
        a, b = data
        return a * b              # S = a * b
    elif shape == "uchburchak":
        b, h = data
        return 0.5 * b * h        # S = ½ * b * h
    return 0

# 2. Natijalarni chiqarish funksiyasi
def display_result(shape, area):
    print(f"\n--- NATIJA ---")
    print(f"{shape.capitalize()} yuzasi: {area:.2f} kvadrat birlik.")
    print("--------------\n")

# 3. Ma'lumotlarni kiritish funksiyasi
def input_data(shape):
    try:
        if shape == "doira":
            r = float(input("Radiusni kiriting: "))
            return [r]
        elif shape == "to'rtburchak":
            a = float(input("Enini kiriting: "))
            b = float(input("Bo'yini kiriting: "))
            return [a, b]
        elif shape == "uchburchak":
            b = float(input("Asosini kiriting: "))
            h = float(input("Balandligini kiriting: "))
            return [b, h]
    except ValueError:
        print("Xato! Faqat son kiriting.")
        return None

# 4. Bosh menyu va dasturni boshqarish
def main_menu():
    while True:
        print("=== GEOMETRIK SHAKLLAR YUZASINI HISOBLASH ===")
        print("1. Doira")
        print("2. To'g'ri to'rtburchak")
        print("3. Uchburchak")
        print("0. Chiqish")
        
        choice = input("Tanlang (0-3): ")
        
        if choice == '0':
            print("Dastur tugatildi. Xayr!")
            break
            
        shapes = {'1': 'doira', '2': "to'rtburchak", '3': 'uchburchak'}
        
        if choice in shapes:
            shape_name = shapes[choice]
            data = input_data(shape_name)
            
            if data:
                area = calculate_area(shape_name, data)
                display_result(shape_name, area)
        else:
            print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.\n")

# Dasturni ishga tushirish
if __name__ == "__main__":
    main_menu()
