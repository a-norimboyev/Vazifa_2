# Palindrom tekshirish (Stack + Queue)
from collections import deque

def is_palindrome(word):
    stack = []
    queue = deque()

    for ch in word:
        stack.append(ch)
        queue.append(ch)

    while stack:
        if stack.pop() != queue.popleft():
            return False

    return True

print(is_palindrome("level"))