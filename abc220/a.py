a, b, c = map(int, input().split())

for n in range(a, b+1):
    if n % c == 0:
        print(n)
        exit()

print(-1)