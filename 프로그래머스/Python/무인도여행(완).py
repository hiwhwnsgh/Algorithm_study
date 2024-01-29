import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)
def solution(maps):
    answer = []
    array = []
    m = []
    for i in maps:
        m.append(list(map(str,i)))
    for i in m:
        print(i)
    def dfs(y,x):
        if x<0 or y<0 or x>=len(m[0]) or y>=len(m) or m[y][x] == 'X':
            return
        array.append(m[y][x])
        m[y][x]='X'
        dfs(y,x-1)
        dfs(y,x+1)
        dfs(y-1,x)
        dfs(y+1,x)
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] !='X':
                array = []
                dfs(i,j)
                answer.append(sum(list(map(int,array))))
    if not answer:
        return [-1]
    answer.sort()
    return answer