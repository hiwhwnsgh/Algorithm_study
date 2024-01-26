import collections
import sys

T = int(sys.stdin.readline())       # 컴퓨터 개수
N = int(sys.stdin.readline())       # 연결선 개수
graph = collections.defaultdict(list)   # 딕셔너리 자료구조
for _ in range(N):
    num,num2 = map(int,sys.stdin.readline().split())    
    graph[num] += [num2]
    graph[num2] += [num]
    # 양방향 간선 연결

array = [1]     # 출발선 
queue = collections.deque([1])  # 경로  
while queue:
    value = queue.popleft()     # 리스트 첫번째인덱스 추출
    for v in graph[value]:
        if v not in array:      # 방문하지 않은 숫자라면
            array.append(v)     
            queue.append(v)     
print(len(array)-1)