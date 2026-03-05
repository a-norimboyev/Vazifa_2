def find_minimum(arr):
    # Massing bronchi elementini min deb olimit
    min_val = arr[0]
    
    # Har bir elementini solishtirib chiai
    for x in arr:
        if x < min_val:
            min_val = x
            
    return min_val

# Berlin massif
numbers = [5, 2, 9, 1, 7]
result = find_minimum(numbers)
print(f"Massivdagi eng kick element: {result}")



""" 
Psevdokod
ALGORITM FindMin(Massiv)
    min = Massiv[0]
    HAR BIR element UCHUN (Massiv ichidagi):
        AGAR element < min BO'LSA:
            min = element
    NATIJA min
OXIRI
"""