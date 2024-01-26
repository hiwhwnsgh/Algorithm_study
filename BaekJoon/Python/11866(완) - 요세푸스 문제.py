import sys
import collections
N,M = map(int,sys.stdin.readline().split())
M-=1
array = [i for i in range(1,N+1)]
deq = collections.deque(array)
result = []
index = 0
while deq:
    if index == M:
        result.append(deq.popleft())
        index = 0
    else:
        num = deq.popleft()
        deq.append(num)
        index +=1
print('<',end='')
for i in range(len(result)-1):
    print(result[i],end=', ')
print(result[len(result)-1],end='')
print('>')