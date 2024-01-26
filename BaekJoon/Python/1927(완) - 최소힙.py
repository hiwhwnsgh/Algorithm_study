import sys
import heapq

heap = []
result = []
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    if not heap and num == 0:
        result.append(0)
        #print(0)
    elif num == 0:
        #print(heapq.heappop(heap))
        result.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap,num)
print(result)

