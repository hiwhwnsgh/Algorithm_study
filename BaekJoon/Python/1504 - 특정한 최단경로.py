import sys
import heapq
import collections

N, E = map(int,sys.stdin.readline().split())
graph = collections.defaultdict(list)
for i in range(E):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int,sys.stdin.readline().split())
dist = collections.defaultdict(int)
Q = [(0,v1)]
while Q:
    time, node = heapq.heappop(Q)
    print(f"time : {time}, node : {node}, Q : {Q}, dist : {dist}")
    if node not in dist:
        dist[node] = time
        for v,w in graph[node]:
            alt = time + w
            heapq.heappush(Q,(alt,v))
if len(dist) == N:
    print(max(dist.values()))
else:
    print(-1)
