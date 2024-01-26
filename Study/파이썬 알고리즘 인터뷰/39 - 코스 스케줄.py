from typing import List
import collections

def canFinish(numCourses: int, prerequisites: List[List[int]])->bool:
    graph = collections.defaultdict(list)
    # 그래프 구성
    for a, b in prerequisites:
        graph[a].append(b)
        
    traced = set()
    visited = set()
    def dfs(i):
        # 순환 구조이면 false
        if i in traced:
            return False
        # 이미 방문했던 노드이면 True
        if i in visited:
            return True
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        # 탐색 종료 후 방문 노드 추가
        visited.add(i)
        return True
    # 순환 구조 판별
    for x in list(graph):
        print(x)
        if not dfs(x):
            return False
    return True
a,b = 2,[[0,1],[1,0]]
print(canFinish(a,b))