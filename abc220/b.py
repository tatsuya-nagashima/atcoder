k = int(input())
a,b = input().split()

A = 0
B = 0
for i in range(len(a)):
    A += k**(len(a)-i-1) * int(a[i])

for i in range(len(b)):
    B += k**(len(b)-i-1) * int(b[i])

ans = A * B
print(ans)