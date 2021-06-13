s = input()
ans = 0

for i in range(10000):
  x = str(i).zfill(4)
  for j, t in enumerate(s):
    if t=="o" and str(j) not in x:
      break
    if t=="x" and str(j) in x:
      break
  else:
    ans += 1
print(ans)