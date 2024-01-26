import sys
from typing import List
def numIsland(grid : List[List[str]]) -> int:
    def dfs(i : int, j:int):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != 1:
            return
        
        grid[i][j] = 0
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i-1,j-1)
        dfs(i-1,j+1)
        dfs(i+1,j-1)
        dfs(i+1,j+1)
        dfs(i,j+1)
        dfs(i,j-1)
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(i,j)
                
                count +=1
    print(grid)
    return count
while True:
    w,h = map(int,sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int,sys.stdin.readline().split())))
    grid_count = numIsland(graph)
    print(grid_count)