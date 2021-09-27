N, S, D = map(int, input().split())

magic = list(map(int, input().split()))
for i in range(len(magic)):
    x, y = magic[i]

    if x < S and y > D:
        print('Yes')
        exit()

print('No') 
