from typing import List
import collections
def findItinerary(tickets : List[List[str]])-> List[str]:
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)
    route = []
    def dfs(a):
        # 첫 번째 값을 읽어 어휘순으로 방문
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)
    dfs('JFK')
    # 다시 뒤집어 어휘 순 결과로
    print(route)
    return route[::-1]
array = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(array)
print(sorted(array))
print(findItinerary(array))