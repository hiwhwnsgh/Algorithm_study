import sys
import heapq

N = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))
Q = []
for i,j in enumerate(array):
    heapq.heappush(Q,(j,i))
result = 0 
total = 0
for i in range(N):
    num = heapq.heappop(Q)
    result = result + num[0]        # 해당 인덱스의 사람이 가지는 소요시간
    total += result               # 한명의 사람이 걸리는 소요시간을 전체 합산
print(total)