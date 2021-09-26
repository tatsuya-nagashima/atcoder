import itertools
def cumsum(arr):
    return list(itertools.accumulate(arr))

N = int(input())
A = list(map(int, input().split()))
X = int(input())

sum_a = sum(A)
div, mod = divmod(X, sum_a)


cum = cumsum(A)
idx = 0
for i in range(len(cum)):
  if cum[i]> mod:
    idx = i+1
    break
ans = div*N + idx
print(ans)