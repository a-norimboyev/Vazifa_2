"""14-vazifa: Bo'lin va zabt et usuli bilan ikki polinomni ko'paytirish.

Polinom koeffitsientlar ro'yxati sifatida ifodalanadi:
  [a0, a1, a2, ...] => a0 + a1*x + a2*x^2 + ...
"""


def poly_multiply_dc(a, b):
    """Ikki polinomni bo'lin va zabt et usuli bilan ko'paytiradi."""
    n = len(a)
    m = len(b)

    if n == 1 or m == 1:
        if n == 1:
            return [a[0] * bj for bj in b]
        return [ai * b[0] for ai in a]

    size = max(n, m)
    if size % 2 != 0:
        size += 1
    a = a + [0] * (size - n)
    b = b + [0] * (size - m)

    half = size // 2
    a_low, a_high = a[:half], a[half:]
    b_low, b_high = b[:half], b[half:]

    z0 = poly_multiply_dc(a_low, b_low)
    z2 = poly_multiply_dc(a_high, b_high)

    a_sum = [a_low[i] + a_high[i] for i in range(half)]
    b_sum = [b_low[i] + b_high[i] for i in range(half)]
    z1_full = poly_multiply_dc(a_sum, b_sum)

    max_len = max(len(z1_full), len(z0), len(z2))
    def pad(lst):
        return lst + [0] * (max_len - len(lst))
    z0_p, z2_p, z1f_p = pad(z0), pad(z2), pad(z1_full)
    z1 = [z1f_p[i] - z0_p[i] - z2_p[i] for i in range(max_len)]

    result_len = 2 * size - 1
    result = [0] * result_len

    for i, val in enumerate(z0):
        result[i] += val
    for i, val in enumerate(z1):
        result[i + half] += val
    for i, val in enumerate(z2):
        result[i + 2 * half] += val

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result


def poly_to_string(coeffs):
    """Polinomni o'qilishi oson ko'rinishga keltiradi."""
    terms = []
    for i, c in enumerate(coeffs):
        if c == 0:
            continue
        if i == 0:
            terms.append(str(c))
        elif i == 1:
            terms.append(f"{c}x")
        else:
            terms.append(f"{c}x^{i}")
    return " + ".join(terms) if terms else "0"


if __name__ == "__main__":
    a = [1, 2, 3]       # 1 + 2x + 3x^2
    b = [4, 5]           # 4 + 5x
    result = poly_multiply_dc(a, b)

    print(f"A(x) = {poly_to_string(a)}")
    print(f"B(x) = {poly_to_string(b)}")
    print(f"A(x) * B(x) = {poly_to_string(result)}")

    a2 = [1, 1, 1, 1]   # 1 + x + x^2 + x^3
    b2 = [1, 1, 1, 1]
    result2 = poly_multiply_dc(a2, b2)
    print(f"\nA(x) = {poly_to_string(a2)}")
    print(f"B(x) = {poly_to_string(b2)}")
    print(f"A(x) * B(x) = {poly_to_string(result2)}")
