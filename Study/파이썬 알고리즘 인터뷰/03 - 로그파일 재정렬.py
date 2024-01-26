from typing import List
def reorderLogFiles(logs : List [str])->List[str]:
    letters, digits = [], []
    for log in logs:
        # print(log)
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    print(letters)
    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key = lambda x: (x.split()[1:],x.split()[0]))
    return letters + digits
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6","let2 own kit dig", "let3 art zero"]

print(reorderLogFiles(logs))