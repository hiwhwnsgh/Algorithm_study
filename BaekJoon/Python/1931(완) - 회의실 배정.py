import sys
import heapq
N = int(sys.stdin.readline())
line = []
for i in range(N):
    array = list(map(int,sys.stdin.readline().split()))
    heapq.heappush(line,(array[1]-array[0]+array[0],array[0],array[1]))
result = [heapq.heappop(line)]
while line:
    array = heapq.heappop(line)
    if result[-1][2] <=array[1]:
        result.append(array)
print(len(result))