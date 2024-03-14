import math
def solution(n, words):
    answer = [words[0]]
    count = 1
    lastAlpha = words[0][-1]
    words.pop(0)
    for word in words:
        count +=1
        if word in answer or lastAlpha != word[0]:
            people = count%n
            if people == 0:
                people = n

            r = count//n
            result = [people,r]
            return result
        answer.append(word)
        lastAlpha = word[-1]
    return [0,0]
