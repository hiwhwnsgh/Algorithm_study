from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for a,b in sorted(tickets,reverse=True):
        graph[a].append(b)
    print(graph)

    def dfs(route):
        while graph[route]:
            dfs(graph[route].pop())
        answer.append(route)
    dfs('ICN')
    print(answer)
    return answer[::-1]