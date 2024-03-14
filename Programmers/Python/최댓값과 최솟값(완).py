def solution(s):
    num = list(map(int,s.split(' ')))
    array = str(min(num)),str(max(num))
    answer = ' '.join(array)
    return answer