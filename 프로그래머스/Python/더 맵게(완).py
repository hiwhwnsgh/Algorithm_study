import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    result = 0
    while scoville[0] < K and len(scoville) > 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville) * 2
        result = first + second
        heapq.heappush(scoville,result)
        answer +=1
    if scoville[0]< K:
        return -1
    return answer
    