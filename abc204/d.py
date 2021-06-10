from math import ceil

n = int(input())
t = list(map(int, input().split()))

s = sum(t)

dp = [[False]*(s+1) for _ in range(n+1)]
dp[0][0] = True
for i in range(n):
    for j in range(s+1):
        dp[i+1][j] |= dp[i][j]
        if j >= t[i]:
            dp[i+1][j] |= dp[i][j-t[i]]

ans = s
for i in range(ceil(s/2), s+1):
    if dp[n][i]:
        ans = i
        break
print(ans)

