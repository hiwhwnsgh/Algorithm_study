import collections
def solution(n, edge):
    answer = 0
    graph = collections.defaultdict(list)
    visit = [0 for i in range(n+1)]
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    Q = collections.deque([[1,0]])
    while Q:
        v,time = Q.popleft()
        if visit[v] == 0:
            visit[v] = time + 1
            for w in graph[v]:
                if visit[w] == 0:
                    Q.append([w,time+1])
    result = max(visit)
    answer = visit.count(result)
    return answer