import collections
def solution(priorities, location):
    priorities = collections.deque(priorities)
    answer = 0
    idx = 0
    length = len(priorities)
    while priorities:
        maxNum = max(priorities)
        num = priorities.popleft()
        if num>=maxNum :
            answer += 1
            priorities.append(-1)
            if location == idx:
                return answer
        else:
            priorities.append(num)
        idx = (idx + 1)% length
    return answer