import sys

n,m,r = map(int,sys.stdin.readline().split()) # 정점, 간선, 시작 정점 입력
graph = [[] for _ in range(n+1)] # 인접리스트 초기화

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)  # 무방향 그래프로 정점 두개 삽입
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort(reverse=True)

visited = [0]*(n+1) # 방문한 정점
stack = [r]
cnt = 1 # 방문순서 카운트
    
while stack:
    v = stack.pop() # 방문한 노드 pop()
    if visited[v] != 0:
        continue
    visited[v] = cnt # 방문한 정점(index)의 방문 순서(cnt) 삽입
    cnt += 1
    for w in graph[v]:
        stack.append(w)

[print(v) for v in visited[1:]]