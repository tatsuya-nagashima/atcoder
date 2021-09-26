s = [input() for _ in range(3)]
t = input()

ans = ''
for i in t:
    ans += s[int(i)-1]

print(ans)