# Qavslarni tekshirish
def is_balanced(expr):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in expr:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0

print(is_balanced("{[()]}"))