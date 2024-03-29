# p. 373 40번 네트워크 딜레이 타임
import heapq
import collections
from typing import List
def networkDelatTime(times : List[List[int]], N : int , K : int) -> int:
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성:
    for u,v,w in times:
        graph[u].append((v,w))

    # 큐 변수 : [(소요시간, 정점)]
    Q = [(0,K)]
    dist = collections.defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    print(graph)
    while Q:
        time, node = heapq.heappop(Q)
        
        if node not in dist:
            dist[node] = time
            for v,w in graph[node]:
                # alt 는 총 가중치, time 현재 가중치, w는 v까지 이동했을 때 필요한 가중치
                alt = time + w          
                heapq.heappush(Q,(alt,v))
        print(Q)
        #print(f"time : {time}, node : {node}, dist : {dist}")
    # 모든 노드의 최단 경로 존재 여부 판별
    if len(dist) == N:
        return max(dist.values())
    return -1
times = [[3,1,5],[3,2,2],[2,1,2],[3,4,1],[4,5,1],[5,6,1],[6,7,1],[7,8,1],[8,1,1]]
N = 8
K = 3
print(networkDelatTime(times,N,K))
