def solution(n):
    answer = 0
    ln = bin(n).count('1')
    print(ln)
    m = n
    while True:
        m += 1
        mln = bin(m).count('1')
        if mln == ln:
            return m
        
            
    return answer