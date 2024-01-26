import sys
from typing import List
def stackSequence(n : int,nums : List[int]):
    stack = [1]
    result = ['+']
    index = 0
    i = 2
    for j in range(n*2):
        if len(result) == n*2:
            break
        if stack == []:
            stack.append(i)
            i+=1
            result.append('+')
            continue
        if nums[index] != stack[-1]:
            stack.append(i)
            result.append('+')
            i+=1
        else:
            stack.pop()
            result.append('-')
            index+=1
    if result.count('+') !=n and result.count('-') != n:
        return 'No'
    return result
n = int(sys.stdin.readline())
array = []
for i in range(n):
    num = int(sys.stdin.readline())
    array.append(num)
result = stackSequence(n,array)
if result == 'No':
    print('NO')
else:
    for i in range(len(result)):
        print(result[i])