n, m, x = map(int, input().split())

A = [ [] for _ in range(n)]
c = [0] * n

INF = 10**9
ans = INF

for i in range(m):
    c_as = list(map(int, input().split()))
    c[i], A[i] = c_as[0], c_as[1:]

for s in range(0, 1 << n):
    smart = [0] * m
    cost = 0
    for i in range(m):
        if(s >> i & 1):
            cost += c[i]
            for j in range(m):
                smart[j] += A[i][j]
    
    ok = True
    for j in range(m):
        if smart[j] < x:
            ok = False
        if ok:
            ans = min(ans, cost)
    
    if ans == INF:
        ans = -1
 
print(ans)