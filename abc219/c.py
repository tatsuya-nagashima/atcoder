X = input()
N = int(input())
S = [input() for _ in range(N)]

def search(S):
    ans = []
    for c in S:
        idx = X.find(c)
        ans.append(idx)
    
    return ans

A = sorted(S,key = search)
for i in A:
    print(i)

    