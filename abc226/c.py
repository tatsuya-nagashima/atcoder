N = int(input())
skill = [list(map(int, input().split())) for _ in range(N)]
learned = [False]*N

import sys
sys.setrecursionlimit(10000)
def dfs(v, t):
  if learned[v] == False:
    for s in skill[v][2:]:
      if learned[s] == False:
        continue
    else:
	    t += skill[v][0]
        learned[v] = True
        
    for pre in skill[v][2:]:
      	if learned[pre]: continue
        else: dfs(pre, t)
    
  return t

ans = 0
for i in range(len(skill)):
  if skill[i][2] == 0:  
    ans += skill[i][0]
    learned[i+1] = True
    break
  
print(dfs(N-1,ans))

