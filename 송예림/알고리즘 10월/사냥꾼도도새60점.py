N = int(input())
H = list(map(int, input().split()))
H = [0] + H

dp = [N for i in range(1001)]
dp[0] = -1
for i in range(N + 1):
    for j in range(len(H)):
        dp[i] = min(dp[i], H[j] + dp[i - j])

print(dp[N])
