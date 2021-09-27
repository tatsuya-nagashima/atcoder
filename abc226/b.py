N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]
print(len(list(map(list, set(map(tuple, line))))))