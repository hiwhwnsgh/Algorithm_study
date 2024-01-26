#p 323
import time



graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3]
}
# 재귀호출을 이용한 DFS 구현
def recusive_dfs(v,discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recusive_dfs(w,discovered)
    return discovered

# 스택을 이용한 반복 구조로 DFS구현
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered
t = time.time()

# 큐를 이용한 반복구조로 BFS 구현
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v= queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered
print(recusive_dfs(1))
print(iterative_dfs(1))