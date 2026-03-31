"""13-vazifa: Ikki nuqtali qidiruv (binary search) bilan sonning kvadrat ildizi."""


def sqrt_binary_search(n, precision=1e-7):
    """n ning kvadrat ildizini belgilangan aniqlikda topadi."""
    if n < 0:
        raise ValueError("Manfiy son uchun haqiqiy kvadrat ildiz mavjud emas")
    if n == 0:
        return 0.0

    low = 0.0
    high = max(1.0, float(n))

    while high - low > precision:
        mid = (low + high) / 2.0
        if mid * mid < n:
            low = mid
        else:
            high = mid

    return (low + high) / 2.0


if __name__ == "__main__":
    test_values = [2, 9, 25, 0.04, 150]
    for val in test_values:
        result = sqrt_binary_search(val)
        print(f"sqrt({val}) = {result:.10f}")
