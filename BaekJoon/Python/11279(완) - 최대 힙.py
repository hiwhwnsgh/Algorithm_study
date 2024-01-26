import sys
import heapq

heap = []
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    if not heap and num == 0:
        print(0)
    elif num == 0:
        print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap,-num)

