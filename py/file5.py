# O‘nlik → ikkilik (Stack)
def decimal_to_binary(n):
    stack = []

    while n > 0:
        stack.append(n % 2)
        n //= 2

    binary = ""
    while stack:
        binary += str(stack.pop())

    return binary

print(decimal_to_binary(5))