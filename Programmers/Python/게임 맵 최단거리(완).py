import collections
def solution(maps):
    xlen = len(maps[0]) - 1
    ylen = len(maps) - 1
    Q = collections.deque([[0,0]])
    answer = 0
    def isCheck(y,x):
        if y<0 or x<0 or y>ylen or x>xlen or maps[y][x] == 0:
            return False
        else:
            return maps[y][x] == 1
    while Q:
        y,x = Q.popleft()
        if isCheck(y-1,x):
            Q.append([y-1,x])
            maps[y-1][x] = maps[y][x] + 1
        if isCheck(y+1,x):
            Q.append([y+1,x])
            maps[y+1][x] = maps[y][x] + 1
        if isCheck(y,x-1):
            Q.append([y,x-1])
            maps[y][x-1] = maps[y][x] + 1
        if isCheck(y,x+1):
            Q.append([y,x+1])
            maps[y][x+1] = maps[y][x] + 1
    if maps[ylen][xlen] == 1:
        return -1
    
    return maps[ylen][xlen]