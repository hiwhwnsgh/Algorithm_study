import sys
import collections
import heapq

V, E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = collections.defaultdict(list)
for i in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))
Q = [(0,K)]
dist = collections.defaultdict(int)
while Q:
    print(Q)
    time, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = time
        for v,w in graph[node]:
            # alt 는 총 가중치, time 현재 가중치, w는 v까지 이동했을 때 필요한 가중치
            alt = time + w          
            heapq.heappush(Q,(alt,v))
for i in range(1,V+1):
    if dist[i] == 0 and i != K:
        print("INF")
    else:
        print(dist[i])