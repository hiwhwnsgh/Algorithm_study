def solution(answers):
    answer = []
    peoples = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    count =[0,0,0]
    for i in range(len(answers)):
        if peoples[0][i%len(peoples[0])] == answers[i]:
            count[0] += 1
        if peoples[1][i%len(peoples[1])] == answers[i]:
            count[1] += 1
        if peoples[2][i%len(peoples[2])] == answers[i]:
            count[2] += 1
    for i in range(3):
        if max(count) == count[i]:
            answer.append(i+1)
    return answer