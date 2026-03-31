"""20-vazifa: Tanga almashtirish — greedy va dinamik dasturlash taqqoslash.

Kanonik tanga tizimlarida (masalan [1,5,10,25]) greedy yechim optimal;
no-kanonik tizimlarda (masalan [1,3,4]) greedy yechim optimal bo'lmasligi mumkin.
"""


def greedy_coin_change(coins, amount):
    """Greedy usul: har doim eng katta tangani tanlaydi."""
    coins_sorted = sorted(coins, reverse=True)
    result = []
    remaining = amount

    for coin in coins_sorted:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin

    if remaining > 0:
        return None
    return result


def dp_coin_change(coins, amount):
    """Dinamik dasturlash: eng kam tangalar sonini topadi."""
    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin

    if dp[amount] == INF:
        return None

    result = []
    cur = amount
    while cur > 0:
        result.append(parent[cur])
        cur -= parent[cur]
    return result


def compare_methods(coin_systems, amounts):
    """Har bir tizim va summa uchun greedy va DP ni taqqoslaydi."""
    print(f"{'Tanga tizimi':<18} {'Summa':<8} {'Greedy':<25} {'DP':<25} {'Natija':<12}")
    print("-" * 90)

    for name, coins in coin_systems:
        for amount in amounts:
            g_result = greedy_coin_change(coins, amount)
            d_result = dp_coin_change(coins, amount)

            g_count = len(g_result) if g_result else "-"
            d_count = len(d_result) if d_result else "-"

            g_str = str(g_result) if g_result else "yechim yo'q"
            d_str = str(d_result) if d_result else "yechim yo'q"

            if g_result and d_result:
                match = "Teng" if len(g_result) == len(d_result) else "FARQ BOR"
            else:
                match = "-"

            print(f"{name:<18} {amount:<8} {g_str:<25} {d_str:<25} {match:<12}")
    print()


if __name__ == "__main__":
    coin_systems = [
        ("Kanonik [1,5,10,25]", [1, 5, 10, 25]),
        ("No-kanonik [1,3,4]", [1, 3, 4]),
        ("No-kanonik [1,6,10]", [1, 6, 10]),
    ]
    amounts = [6, 12, 15, 30]

    compare_methods(coin_systems, amounts)

    print("=== Xulosa ===")
    print("Kanonik tizimlarda greedy va DP bir xil natija beradi.")
    print("No-kanonik tizimlarda greedy optimal bo'lmasligi mumkin —")
    print("faqat DP har doim eng kam tangalar sonini kafolatlaydi.")
