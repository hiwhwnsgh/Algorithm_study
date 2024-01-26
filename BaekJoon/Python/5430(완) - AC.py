import re
import sys
import collections
T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline().rstrip()
    count = int(sys.stdin.readline())
    array = sys.stdin.readline().rstrip()
    array = re.findall('\d+',array)
    array = list(map(int,array))
    deq = collections.deque(array)
    num = 0
    tf = False
    for i in p:
        if i == 'R':
            num+=1
        else:
            if deq:
                if num % 2 == 0:
                    deq.popleft()
                else:
                    deq.pop()
            else:
                print('error')
                tf = True
                break
    if tf:
        continue
    if deq:
        print('[',end='')
        if num % 2 == 0:
            for i in range(len(deq)-1):
                print(deq[i],end=',')
            print(deq[len(deq)-1],end=']\n')
        else:
            for i in range(len(deq)-1,0,-1):
                print(deq[i],end=',')
            print(deq[0],end=']\n')
    else:
        print('[]')
    