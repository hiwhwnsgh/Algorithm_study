import collections
def solution(arr):
    arr= collections.deque(arr)
    answer = [arr.popleft()]
    while arr:
        v = arr.popleft()
        if answer[-1] != v:
            answer.append(v)
    return answer