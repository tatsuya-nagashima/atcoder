from collections import deque

N = int(input())
A = list(map(int, input().split()))

que = deque()
for a in reversed(A):
    que.appendleft(a)

dp = [[0]*10 for _ in range(N)]
while len(que) > 0:
    x = que.popleft()
    y = que.popleft()

    xy = (x+y)%10
    xy = (x*y)%10
    que.appendleft(xy)

if 