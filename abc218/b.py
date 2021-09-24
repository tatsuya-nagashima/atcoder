P = list(map(int,input().split()))
chars = list(map(lambda x: chr(x-1+ord('a')), P))

print(''.join(chars))