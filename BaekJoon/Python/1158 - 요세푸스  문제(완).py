import sys
import collections
N, K = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, N+1)]
arr = collections.deque(arr)
result = []
while arr:
    for _ in range(K-1):
        arr.append(arr.popleft())
    result.append(arr.popleft())
print("<", end='')
for i in range(len(result)-1):
    print(result[i], end=", ")
print(result[-1],end="")
print(">")
