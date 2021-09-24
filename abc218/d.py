N = int(input())
points = set(tuple(map(int,input().split())) for _ in range(N))

ans = 0 
for p1 in points:
    for p2 in points:
        if not (p1[0] < p2[0] and p1[1] < p2[1]):
            continue
        
        q = (p1[0], p2[1])
        r = (p2[0], p1[1])

        if q in points and r in points:
            ans += 1

print(ans)