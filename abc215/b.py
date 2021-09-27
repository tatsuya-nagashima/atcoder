N = int(input())

ans = 0
K = 0
while 2**K <= N:
  ans = K
  K+=1

print(ans)