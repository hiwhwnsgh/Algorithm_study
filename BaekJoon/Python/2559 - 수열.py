import sys

N,K = map(int,sys.stdin.readline().split())
M = list(map(int,sys.stdin.readline().split()))
maxValue = -sys.maxsize
total = 0
result = []
for i in range(N):
    total += M[i]
    result.append(total)
print(result)