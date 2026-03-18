# Stack klass va metodlar
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


stack = Stack()
for i in range(1, 6):
    stack.push(i)

print("Size:", stack.size())
print("Top:", stack.peek())
print("Pop:", stack.pop())
print("Empty:", stack.is_empty())