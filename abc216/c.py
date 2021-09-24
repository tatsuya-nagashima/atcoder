n = int(input())

s = ''
while n > 0:
    q = n % 2
    if q == 0 :
        s += 'B'
    else:
        s += 'A'
    n //= 2

ans = s[::-1]
print(ans)