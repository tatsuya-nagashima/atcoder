S = input()
Smin, Smax = S,S
l, r = S, S

for i in range(len(S)):
  l = S[i:] + S[0:i]
  r = S[len(S)-i:] + S[:len(S)-i]
  if l < Smin:
    Smin = l
  if r < Smin:
    Smin = r
  if l > Smax:
    Smin = l
  if r > Smax:
    Smax = r
    
print(Smin)
print(Smax)
  