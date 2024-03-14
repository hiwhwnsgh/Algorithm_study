def solution(n):
    answer = []
    def hanoi(n,first,two,third):
        if n==1:
            answer.append([first,third])
            return
        hanoi(n-1,first,third,two)
        answer.append([first,third])
        hanoi(n-1,two,first,third)
    hanoi(n,1,2,3)
        
    
    return answer