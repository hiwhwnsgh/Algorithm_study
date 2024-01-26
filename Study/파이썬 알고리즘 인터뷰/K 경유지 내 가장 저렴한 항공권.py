# p. 379 
# 41번 K 경유지 내 가장 저렴한 항공권
from typing import List
import collections
import heapq
def findCheapestPrice(n: int, flights : List[List[int]], src : int, dst:int, K:int) -> int:
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u,v,w in flights:
        graph[u].append((v,w))
    
    # 큐 변수 : [(가격, 정점, 남은 가능 경유지 수)]
    Q = [(0,src,K)]
    print(graph)
    # 우선순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
    while Q:
        print('Q : ',Q)
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k>=0:
            for v,w in graph[node]:
                alt = price + w
                heapq.heappush(Q,(alt,v,k-1))
    return -1
n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
K = 1
print(findCheapestPrice(n,edges,src,dst,K))