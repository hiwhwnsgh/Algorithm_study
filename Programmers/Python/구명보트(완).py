def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    print(people)
    for p in people:
        if p+people[-1] <= limit:
            people.pop()
            answer += 1
        else:
            answer += 1
    return answer