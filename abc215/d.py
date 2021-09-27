import math

N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i in range(1, M+1):
    for a in A:
        if not math.gcd(a, i) == 1:
            continue
        if a == A[-1]:
            ans.append(i)