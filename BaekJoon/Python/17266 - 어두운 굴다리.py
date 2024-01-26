import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
x = list(map(int,sys.stdin.readline()))
left,right = 0,N
while left<=right:
    mid = (left+right) // 2
    
