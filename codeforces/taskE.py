
def solve():
    n, m = map(int, input().split())
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j]
            dp[i] %= m

    print(dp[n])


def main():
    solve()


main()
