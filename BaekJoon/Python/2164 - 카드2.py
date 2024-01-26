import sys
import collections
N= int(sys.stdin.readline())
array = list(range(1,N+1))
array = collections.deque(array)
for i in range(N-1):
    array.popleft()
    num = array.popleft()
    array.append(num)
print(array[0])