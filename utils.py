# h,w = map(int, input().split())
# matrix = [list(input()) for _ in range(h)]

# directions = [[0, 1], [1,1], [1, 0], [1, -1], [0, -1], [-1,-1],[-1, 0],[-1, 1]]
# for r in range(h):
#   for c in range(w):
#     count = 0
#     if matrix[r][c] == ".":
#       for dx, dy in directions:
#         if 0 <= r + dx <= h - 1 and 0<= c + dy <= w - 1 and matrix[r + dx][c + dy] == "#":
#           count += 1
#       matrix[r][c] = str(count)
# for i in matrix:
#   print(str("".join(i)))

import sys
sys.setrecursionlimit(10000)
def dfs(G, v, seen):
    seen[v]=True
    for next_v in G[v]:
        if seen[next_v]: continue
        dfs(G, next_v, seen)
    return seen

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

import itertools
def cumsum(arr):
    return list(itertools.accumulate(arr))

def ssp(dp):
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            dp[i+1][j] |= dp[i][j]
            if j >= t[i]:
                dp[i+1][j] |= dp[i][j-t[i]]
    return dp