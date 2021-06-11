N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

D =[0]*N
for j in range(N):
    D[j] = B[C[j]-1]

cnt =[0]*N
for j in range(N):
    cnt[D[j]]+=1

ans=0
for i in range(N):
    ans+=cnt[A[i]]

print(ans)