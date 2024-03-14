def solution(sizes):
    maxF = 0
    maxS = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
    
    for i in range(len(sizes)):
        maxF = max(sizes[i][0],maxF)
        maxS = max(sizes[i][1],maxS)
    return maxF * maxS