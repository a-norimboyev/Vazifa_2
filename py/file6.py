# Kafe navbati (Queue simulyatsiya)
from collections import deque

queue = deque()

queue.append("Buyurtma 1")
queue.append("Buyurtma 2")
queue.append("Buyurtma 3")

while queue:
    print("Bajarildi:", queue.popleft())