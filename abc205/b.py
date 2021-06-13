import sys

N = int(input())
A = list(map(int, input().split()))

A.sort() 
for i in range(len(A)-1):
    if A[i+1] - A[i] != 1:
        print("No")
        sys.exit()

print("Yes")