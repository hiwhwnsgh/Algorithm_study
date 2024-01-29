def solution(numbers, target):
    answer = []
    def dfs(csum,index,path):
        if index>=len(numbers):
            if csum == target:
                answer.append(path)    
            return
        dfs(csum+numbers[index],index+1,path+[numbers[index]])
        dfs(csum-numbers[index],index+1,path+[-numbers[index]])
            
            
    dfs(0,0,[])
    return len(answer)