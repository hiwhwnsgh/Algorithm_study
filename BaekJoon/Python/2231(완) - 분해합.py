import sys

N = int(sys.stdin.readline())
l = []
for i in range(N):
    array = list(map(int,str(i)))
    result = sum(array) + i
    if result == int(N):
        l.append(i)         #  == l.append(int(''.join(map(str,array)))
if l:
    print(min(l))
else:
    print(0)