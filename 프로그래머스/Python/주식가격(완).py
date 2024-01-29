from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    idx = 0
    while prices:
        count = 0
        v = prices.popleft()
        for i in prices:
            count+=1
            if v > i:
                break
        answer.append(count)
    return answer