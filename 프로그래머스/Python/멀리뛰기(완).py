def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return solution(n-1) + solution(n-2)