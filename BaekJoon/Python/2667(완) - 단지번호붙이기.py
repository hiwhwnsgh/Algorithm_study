import sys
from typing import List
N = int(sys.stdin.readline())
array = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
class solution:
    num = 0
    result = []
    def HomeCheck(self,grid : List[List[int]])-> List:
        def dfs(x,y):
            if x<0 or y<0 or x>=len(array[0]) or y>=len(array) or grid[x][y] != 1:
                return count
            grid[x][y] = 0
            self.num += 1
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i,j)
                    self.result.append(self.num)
                    self.num = 0
                    count+=1
        return count
    def getHome(self):
        return sorted(self.result)
        
ob = solution()
count = ob.HomeCheck(array)
value = ob.getHome()
print(count)
for i in value:
    print(i)