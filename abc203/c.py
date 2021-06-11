N,K=map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
AB.sort()

ans = K
for i in AB:
  if i[0]<=K:
    K+=i[1]
  else:
    break
  
print(K) 