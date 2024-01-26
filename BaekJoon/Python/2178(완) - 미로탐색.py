import sys
import collections
from typing import List
N,M = map(int,sys.stdin.readline().split())

array = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
q = collections.deque()
def checkIndex(y,x):
    if x<0 or y<0 or x>=M or y>=N:
        return False
    else:
        return array[y][x] == 1
q.append([0,0,1])
while q:
    y,x,count = q.popleft()
    if y == len(array) - 1 and x == len(array[0])-1:
        break
    if checkIndex(y,x+1):
        q.append([y,x+1,count+1])
        array[y][x+1] = 9
    if checkIndex(y,x-1):
        q.append([y,x-1,count+1])
        array[y][x-1] = 9
    if checkIndex(y+1,x):
        q.append([y+1,x,count+1])
        array[y+1][x] = 9
    if checkIndex(y-1,x):
        q.append([y-1,x,count+1])
        array[y-1][x] = 9
print(count)