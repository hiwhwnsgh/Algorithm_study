def solution(arr):
    def gcd(x,y):
        while y:
            x,y = y,x%y
        return x
    
    while len(arr)>1:
        a = arr.pop()
        b = arr.pop()
        num = gcd(a,b)
        arr.append(a*b//num)
        print(arr)
    
    answer = arr[0]
        
    return answer