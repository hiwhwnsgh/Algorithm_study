import sys
import collections
N,K = map(int,sys.stdin.readline().split())

def BFS(n,k):
    queue = collections.deque([(n,0)])
    visited = set()
    while queue:
        value,time = queue.popleft()
        if value == k:
            return time
        for caseNum in [value*2,value+1,value-1]:
            if caseNum not in visited and caseNum <= 100000:
                visited.add(caseNum)
                queue.append((caseNum,time+1))
print(BFS(N,K))