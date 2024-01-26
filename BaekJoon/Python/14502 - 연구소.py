import sys

N, M = map(int,sys.stdin.readline().split())
array = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
print(array)