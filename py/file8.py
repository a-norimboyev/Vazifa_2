def draw_rectangle(width, height, symbol):
    """
    Berilgan o'lcham va belgi asosida to'g'ri to'rtburchak chizadi.
    width: eni (belgilar soni)
    height: bo'yi (qatorlar soni)
    symbol: ishlatiladigan belgi
    """
    for i in range(height):
        # Belgini width marta yonma-yon chiqaradi
        print(symbol * width)

# Protsedurani sinab ko'ramiz:
print("Misol 1 (5x3 o'lchamda, '*' belgisi bilan):")
draw_rectangle(5, 3, "*")

print("\nMisol 2 (10x2 o'lchamda, '#' belgisi bilan):")
draw_rectangle(10, 2, "#")
