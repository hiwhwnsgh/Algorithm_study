import sys
import collections
N,M,K,X = map(int,sys.stdin.readline().split())
graph = collections.defaultdict(list)
for i in range(1,M+1):
    graph[i] = []
for _ in range(M):
    start,end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
result = []
queue = collections.deque([[X,1]])
discovered = []
while queue:
    node,time = queue.popleft()
    for v in graph[node]:
        if v not in discovered:
            discovered.append(v)
            queue.append([v,time+1])
            if time == K:
                result.append(v)
result.sort()
print(discovered)
if len(result) == 0:
    print(-1)
else:
    for value in result:
        print(value)
