import sys

N,M = map(int,sys.stdin.readline().split())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()
