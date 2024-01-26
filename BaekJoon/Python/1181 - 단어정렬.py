import sys

n =  int(sys.stdin.readline())
array = []
for i in range(n):
    array.append(sys.stdin.readline().rstrip())
array.sort()
array.sort(key=len)
result = []
for i in array:
    if  i not in result:
        result.append(i)
for value in result:
    print(value)