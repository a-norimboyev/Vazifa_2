# Psevdokod
"""
ALGORITM SelectionSort(Massiv)
    n = Massiv uzunligi
    FOR i = 0 TO n-1:
        min_index = i
        FOR j = i+1 TO n-1:
            IF Massiv[j] < Massiv[min_index]:
                min_index = j
        SWAP(Massiv[i], Massiv[min_index])
OXIRI
"""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Hozircha i-chi elementni eng kichik deb olamiz
        min_idx = i
        
        # Undan keyingi qismdan eng kichigini qidiramiz
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Topilgan eng kichik elementni i-chi o'rin bilan almashtiramiz
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Sinov uchun:
numbers = [5, 2, 9, 1, 7]
print("Saralangan massiv:", selection_sort(numbers))