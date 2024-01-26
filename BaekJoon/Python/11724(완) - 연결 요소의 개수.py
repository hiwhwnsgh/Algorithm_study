import sys
import collections

def connect(graph,i,visited):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            connect(graph,j,visited)
    

graph = collections.defaultdict(list)
N,M = map(int,sys.stdin.readline().split())
count = 0
for i in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * (N+1)
for i in range(1,N+1):
    if not visited[i]:
        connect(graph,i,visited)
        count += 1
print(count)