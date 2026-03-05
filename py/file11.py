def calculate_average(number_list):
    if not number_list: # Ro'yxat bo'sh bo'lsa xatolik bermasligi uchun
        return 0
    
    total_sum = sum(number_list)
    count = len(number_list)
    return total_sum / count

# Sinab ko'ramiz:
numbers = [10, 20, 30, 40, 50]
print(f"O'rtacha qiymat: {calculate_average(numbers)}") # Natija: 30.0
