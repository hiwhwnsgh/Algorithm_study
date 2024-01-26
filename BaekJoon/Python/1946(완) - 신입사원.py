import sys
"""
첫번째 성공작
import heapq
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    count = 1
    heap = []
    for _ in range(N):
        a,b =map(int,sys.stdin.readline().split())
        heapq.heappush(heap,(a,b))
    array = heapq.heappop(heap)
    for _ in range(N-1):
        num = heapq.heappop(heap)
        if array[0] >= num[0] or array[1] >= num[1]:
            count+=1
            array = num
    print(count)
"""

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    count = 0
    array = []
    for _ in range(N):
        array.append(list(map(int,sys.stdin.readline().split())))
    array.sort()
    result = array[0]
    for arr in array:
        if result[0] >= arr[0] or result[1] >= arr[1]:
            count+=1
            result = arr
    print(count)