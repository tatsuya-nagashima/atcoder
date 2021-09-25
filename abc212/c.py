from bisect import bisect_right

INF = 10 ** 10

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split())) + [-INF, INF]

A.sort()
B.sort()

ans = INF
for a in A:
    pos = bisect_right(B, a)
    ans = min(ans, abs(B[pos] - a))
    ans = min(ans, abs(B[pos-1] - a))

print(ans)
