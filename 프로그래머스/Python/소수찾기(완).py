import math
def solution(numbers):
    result = []
    prev_elements=[]
    answer = []
    numbers = list(map(int,numbers))
    def dfs(elements):
        if prev_elements and prev_elements not in result and sum(prev_elements) > 1:
            result.append(prev_elements[:])
        for i in elements:
            next_elements = elements[:]
            next_elements.remove(i)
            prev_elements.append(i)
            dfs(next_elements)
            prev_elements.pop()
    def sosu(num):
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    dfs(numbers)

    for i in result:
        s = ''.join(str(s) for s in i)
        s = int(s)
        if sosu(s):
            if s not in answer:
                answer.append(s)
                
    
    return len(answer)