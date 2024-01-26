import sys
import collections
number = int(sys.stdin.readline())
for _ in range(number):
    N,M = map(int,sys.stdin.readline().split())
    array = list(map(int,sys.stdin.readline().split()))
    array2 = []
    for i,j in enumerate(array):
        array2.append([j,i])
    deq = collections.deque(array)
    deq2 = collections.deque(array2)
    if N == 1:
        print(1)
        continue
    count = 0
    while deq:
        if deq[0] == max(deq):
            deq.popleft()
            num = deq2.popleft()
            count+=1
            if num[1] == M:
                break
        else:
            deq.append(deq.popleft())
            deq2.append(deq2.popleft())
    print(count)