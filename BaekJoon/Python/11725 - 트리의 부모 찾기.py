import sys
import collections

graph = collections.defaultdict(int)
N = int(sys.stdin.readline())
for _ in range(N-1):
    root,node = map(int,sys.stdin.readline().split())
    graph[root] = node


