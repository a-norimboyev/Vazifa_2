# Satrni teskari qilish (Stack)
def reverse_string(s):
    stack = []
    for ch in s:
        stack.append(ch)

    reversed_str = ""
    while stack:
        reversed_str += stack.pop()

    return reversed_str

print(reverse_string("salom"))