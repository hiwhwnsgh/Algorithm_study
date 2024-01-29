def solution(brown, yellow):
    answer = [5000,1]
    caffet = brown + yellow
    for i in range(2,caffet//2):
        if caffet % i == 0 and i - caffet//i >= 0 and i-caffet//i < answer[0] - answer[1]:
            answer[0] = i
            answer[1] = caffet//i
    return answer