import sys
import collections
N, M = map(int,sys.stdin.readline().split())
array = [i for i in range(1,N+1)]
deq = collections.deque(array)
position = list(map(int,sys.stdin.readline().split()))
count = 0
index = 0
while index<M:
    if position[index] == deq[0]:
        deq.popleft()
        index += 1
    else:
        for i in range(len(deq)):
            if position[index] == deq[i]:
                num = i
                break
        if num <= len(deq)//2:
            deq.append(deq.popleft())
        else:
            deq.appendleft(deq.pop())
        count += 1
print(count)
