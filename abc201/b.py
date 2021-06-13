N = int(input())
mountain = []

for i in range(N):
  S,T=map(str,input().split())
  T = int(T)
  mountain.append([T,S])

mountain.sort(reverse=True)
print(mountain[1][1])