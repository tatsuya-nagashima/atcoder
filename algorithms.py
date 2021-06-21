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