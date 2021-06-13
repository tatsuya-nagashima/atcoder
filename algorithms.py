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
            if dist[next_v] is None:
                dist[next_v] = dist[v] + 1
                queue.append(next_v)
    return dist

#累積和
import itertools
def cumsum(arr):
    return list(itertools.accumulate(arr))

#部分和問題
def ssp(dp):
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            dp[i+1][j] |= dp[i][j]
            if j >= t[i]:
                dp[i+1][j] |= dp[i][j-t[i]]
    return dp

#二分探索
def binary_search(arr, key):
    left = -1
    right = len(arr)

    while right - left > 1 :
        mid = left + (right - left) / 2;

        if arr[mid] >= key: right = mid
        else: left = mid
    
    return right
