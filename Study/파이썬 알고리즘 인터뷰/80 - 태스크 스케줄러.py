from typing import List
import collections

#우선순위 큐 사용
def leastInterval(tasks:List[str], n : int) -> int:
    counter = collections.Counter(tasks)
    result = 0
    while True:
        sub_count = 0
        # 개수 순 출력
        for task, _ in counter.most_common(n+1):
            #print(task,_,sub_count)
            sub_count +=1
            result +=1
            counter.subtract(task)          #튜플에서 값 1 제거 ex) (A,3) -> (A,2)

            
            counter +=collections.Counter() #0이하인 아이템을 목록에서 완전히 제거
        
        if not counter:
            break
        result += n - sub_count + 1         # idle ??
    return result
task = ["A","A","A","B","C","D"]
n = 2
print(leastInterval(task,n))