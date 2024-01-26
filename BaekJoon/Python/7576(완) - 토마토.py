import sys
import collections
N,M = map(int,sys.stdin.readline().split())
array = []
for i in range(M):
    array.append(list(map(int,sys.stdin.readline().split())))
def IsCheck(y,x):
    if y <0 or x<0 or y>=M or x>=N:
        return False
    else:
        return array[y][x] == 0
idx = []
for i in range(len(array)):
    while 1 in array[i]:
        idx.append([i,array[i].index(1),0])
        array[i][idx[-1][1]] = 9
q = collections.deque()
for i in idx:
    q.append(i)
while q:
    y,x,count = q.popleft() 
    if IsCheck(y,x-1):
        q.append([y,x-1,count+1])
        array[y][x-1] = 9
    if IsCheck(y,x+1):
        q.append([y,x+1,count+1])
        array[y][x+1] = 9
    if IsCheck(y-1,x):
        q.append([y-1,x,count+1])
        array[y-1][x] = 9
    if IsCheck(y+1,x):
        q.append([y+1,x,count+1])
        array[y+1][x] = 9
tf = True
for i in array:
    if 0 in i:
        tf = False
if tf:
    print(count)
else:
    print(-1)

