def generate_fibonacci(n):
    if n <= 0: return []
    if n == 1: return [0]
    
    fib_list = [0, 1]
    while len(fib_list) < n:
        # Oxirgi ikki elementni qo'shib, yangisini hosil qilamiz
        next_val = fib_list[-1] + fib_list[-2]
        fib_list.append(next_val)
        
    return fib_list

# Sinab ko'ramiz:
print(f"Dastlabki 8 ta Fibonachchi soni: {generate_fibonacci(8)}")
