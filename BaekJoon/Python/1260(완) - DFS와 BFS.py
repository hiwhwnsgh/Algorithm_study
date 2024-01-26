from dis import disco
import sys
import collections
graph = collections.defaultdict(list)
def dfs(v,discovered =[]):
    discovered.append(v)
    for i in graph[v]:
        if i not in discovered:
            discovered = dfs(i,discovered)
    return discovered

def bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if i not in discovered:
                discovered.append(i)
                queue.append(i)
    return discovered

N,M,V = map(int,sys.stdin.readline().split())
for i in range(1,M+1):
    graph[i] = []
for i in range(M):
    m,num = map(int,sys.stdin.readline().split())
    graph[m].append(num)
    graph[num].append(m)
for i in range(M):
    graph[i].sort()
print(*dfs(V))
print(*bfs(V))