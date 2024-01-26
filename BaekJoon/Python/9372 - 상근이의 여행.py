import sys
import collections


T = int(sys.stdin.readline())
for i in range(T):
    N,M = map(int,sys.stdin.readline().split())
    graph = collections.defaultdict(list)
    count = -1
    visited = [False] * (N+1)
    [graph[i] for i in range(1,N+1)]
    for _ in range(M):
        u,w = map(int,sys.stdin.readline().split())
        graph[u].append(w)
        graph[w].append(u)
    
    for i in range(1,N+1):
        stack = [i]    
        while stack:
            idx = stack.pop()
            if not graph[idx]:
                break
            for j in graph[idx]:
                if not visited[j]:
                    visited[j] = True
                    stack.append(j)
                    count += 1
    print(count)

    
