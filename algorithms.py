#深さ優先探索
import sys
sys.setrecursionlimit(10000)
def dfs(G, v, seen):
    seen[v]=True
    for next_v in G[v]:
        if seen[next_v]: continue
        dfs(G, next_v, seen)
    return seen

#幅優先探索
from collections import deque
def bfs(G, u, dist):
    dist[u] = 0 
    queue = deque([u])
    while queue:
        v = queue.popleft()
        for next_v in G[v]:
            if dist[next_v] == -1:
                dist[next_v] = dist[v] + 1
                queue.append(next_v)
    return dist

#累積和
import itertools
def cumsum(arr):
    return list(itertools.accumulate(arr))

#部分和問題
def ssp(dp, arr, N, A):
    dp[0][0] = True
    for i in range(N):
        for j in range(A+1):
            dp[i+1][j] |= dp[i][j]
            if j >= arr[i]:
                dp[i+1][j] |= dp[i][j-arr[i]]
    return dp

#二分探索
def binary_search_left(arr, key):
  left = -1
  right = len(arr)
  while right - left >1:
    mid = (left + right)//2
    if arr[mid] >= key: right = mid
    else: left = mid
    
  return right

def binary_search_right(arr, key):
  left = -1
  right = len(arr)
  while right - left >1:
    mid = (left + right)//2
    if arr[mid] > key: right = mid
    else: left = mid
    
  return right  

#エラトステネスの篩
def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    data = list(range(0, n + 1))
    for i in range(2, int(n**0.5) + 1):
        if data[i] > 0:
            for j in range(i**2, n + 1, i):
                data[j] = 0
    return [i for i in range(2, n + 1) if data[i] > 0]


from collections import deque
import collections

n, m = map(int, input().split())

ab = []

graph = [[] for _ in range(n+1)]
for i in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)
  ab.append((u, v))

check = 0

#まず、次数が３以上のものがあればNG
for i in range(n+1):
  if len(graph[i]) >= 3:
    check = 1
    break

#UnionFindの定形
par = [-1]*(n+1) #負なら親で、その絶対値が連結のサイズ。
 
def find(x):#xの親を求める
  X = x
  while par[X] >= 0: #親にたどり着くまで、つまり、parが負になるまでparをたどる。
    X = par[X]
  return X #最後、parが負になるようなXがxの親になる。
def same(x,y):
  return find(x) == find(y)
def unite(x,y):#xが含まれるグループとyが含まれるグループをくっつける
  X = find(x) #xが含まれるグループの親はX
  Y = find(y) #yが含まれるグループの親はY
  if X == Y:
    return 0
  else:
    if par[X] > par[Y]: #Xのグループのサイズが小さいときは文字を入れ替える（※負数であることに注意）
      X,Y = Y,X
    par[X] += par[Y] #サイズの大きいXのグループに、Yのグループのサイズを加える。
    par[Y] = X #Yのほうは「子」になったので、「Yの親はX」という情報に変更する（findでたどれるように）
def size(x):
  return -par[find(x)]
#ここまでUnionFindの定形

#閉路があればNG。sameで判定できる
for a, b in ab:
  if same(a, b):
    check = 1
  unite(a, b)

if check == 0:
  print("Yes")
else:
  print("No")

#順列全探索
import itertools
n = 3
for p in itertools.permutations(range(n)):
  print(p)