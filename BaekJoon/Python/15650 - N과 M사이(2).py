import sys
from typing import List

def combine(nums : List, m :int) -> List[int]:
    result = []
    def dfs(elements,start,m):
        if m == 0:
            result.append(elements[:])
            return
        for i in range(start, len(nums)+1):
            elements.append(i)
            dfs(elements,i+1,m-1)
            elements.pop()
    dfs([],1,m)
    return result
n,m = map(int,sys.stdin.readline().split())
nums = [i for i in range(1,n+1)]
result = combine(nums,m)
for i in result:
    print(*i)