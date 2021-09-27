import itertools

S, N = input().split()
N = int(N)

all = set(itertools.permutations(S, len(S)))
all = sorted(all)
ans = ''.join(all[N-1])
print(ans)