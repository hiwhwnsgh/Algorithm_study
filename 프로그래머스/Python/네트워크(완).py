from collections import deque
def solution(n, computers):
    count = 0
    visited = [False for i in range(n)]
    def dfs(i,visited):
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                visited[j] = True
                dfs(j,visited)
                
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            count +=1
            dfs(i,visited)
    

    return count