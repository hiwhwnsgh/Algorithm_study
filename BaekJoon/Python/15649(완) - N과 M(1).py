import sys
from typing import List
def permute(nums : List[int],m) -> List[List[int]]:
    results = []
    prev_element = []
    def dfs(elements,m):
        if m == 0:
            results.append(prev_element[:])
        for e in elements:
            next_element = elements[:]
            next_element.remove(e)          
            prev_element.append(e)
            dfs(next_element,m-1)
            prev_element.pop()
    dfs(nums,m)
    return results
n,m = map(int,sys.stdin.readline().split())
n = [i for i in range(1,n+1)]
array = permute(n,m)
for i in array:
     print(*i)