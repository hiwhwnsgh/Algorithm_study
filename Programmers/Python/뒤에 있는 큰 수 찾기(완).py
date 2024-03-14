def solution(numbers):
    answer = [-1 for i in range(len(numbers))]
    stack = []
    for i,j in enumerate(numbers):
        while stack and j > numbers[stack[-1]]:
            print(stack)
            top = stack.pop()
            answer[top] = j
        stack.append(i)
    return answer