def max_profit_with_fee(prices: list[int], fee: int) -> int:
    """
    Return maximum profit by buying and selling stocks with transaction fee fee
    """
    prices.append(-fee)
    ans = 0
    mn = prices[0]
    mx = prices[0]
    for i in range(1, len(prices)):
        if prices[i] + fee <= mx or prices[i] <= mn:
            ans += max(0, mx - mn - fee)
            mx = mn = prices[i]
        else:
            mx = max(mx, prices[i])

    return ans


def max_profit_with_cooldown(prices: list[int], cooldown: int) -> int:
    """
    Return maximum profit by buying and selling stocks with at least one day cooldown after last selling.
    Time complexity is O(n), where n is number of days.
    """
    n = len(prices)
    rest = [0] * n  # rest in the day i.
    sell = [0] * n  # sell in the day i.
    buy = [0] * n  # buy in the day i.

    # base cases, in the first day
    rest[0] = 0
    buy[0] = -prices[0]
    sell[0] = float('-inf')

    for i in range(1, n):
        # yesterday should sell or rest
        rest[i] = max(sell[i-1], rest[i-1])
        # consider yesterday's buying or buy today
        buy[i] = max(buy[i-1], rest[i-1] - prices[i])
        # yesterday should buy
        sell[i] = buy[i-1] + prices[i]

    return max(rest[-1], sell[-1])

















