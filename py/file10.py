# Brauzer tarixi (2 ta stack)
back_stack = []
forward_stack = []

def visit(page):
    back_stack.append(page)
    forward_stack.clear()

def back():
    if len(back_stack) > 1:
        forward_stack.append(back_stack.pop())
    return back_stack[-1]

def forward():
    if forward_stack:
        back_stack.append(forward_stack.pop())
    return back_stack[-1]


visit("Google")
visit("YouTube")
visit("ChatGPT")

print("Back:", back())
print("Forward:", forward())