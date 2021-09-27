N, M = map(int, input().split())
dishes = [tuple(map(int, input().split())) for _ in range(M)]
K = int(input())
bowls= [tuple(map(int, input().split())) for _ in range(K)]

ans = 0
for i in range(1 << K):
    use = [False] * (N+1)
    for j in range(K):
        if ((i >> j) & 1):
            use[bowls[j][0]] = True
        else:
            use[bowls[j][1]] = True

    conditons = 0
    for a,b in dishes:
        if use[a] and use[b]:
            conditons += 1
    ans = max(ans, conditons)
    
print(ans)