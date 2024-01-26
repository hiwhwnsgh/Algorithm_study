import sys
import heapq
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    cardCount = int(sys.stdin.readline())
    heapq.heappush(heap,cardCount)
result = 0
while heap:
    firstNum = heapq.heappop(heap)
    if not heap:
        break
    secondNum = heapq.heappop(heap)
    print(firstNum,secondNum)
    add = firstNum + secondNum
    result += add
    heapq.heappush(heap,add)

print(result,heap)
