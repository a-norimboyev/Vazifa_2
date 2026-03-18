# Queue klass
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def front(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.front())
print(q.dequeue())
print(q.size())