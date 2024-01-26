from typing import List
import sys
sys.setrecursionlimit(10000)        # 재귀 깊이 제한 변경 함수
def cabbageCheck(grid:List[List[int]]) -> int:
    def dfs(x,y):
        if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y] != 1:
            return
        grid[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(i,j)
                count+=1
    return count
T = int(sys.stdin.readline())

for _ in range(T):
    M,N,K = map(int,sys.stdin.readline().split())
    array = [[0 for j in range(M)] for i in range(N)]
    for n in range(K):
        x,y = map(int,sys.stdin.readline().split())
        array[y][x] = 1
    print(cabbageCheck(array))
