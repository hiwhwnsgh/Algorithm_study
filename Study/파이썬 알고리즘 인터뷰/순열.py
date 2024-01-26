from typing import List
import itertools
def permute(nums : List[int]) -> List[List[int]]:
    results = []
    prev_elements = []

    def dfs(elements):
        # 리프 노드일 때 결과 추가
        if len(elements) == 0:
            results.append(prev_elements[:])
        
        # 순열 생성 재귀 호출
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)
            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()
    dfs(nums)
    return results
def itertools_permute(nums : List):
    return list(itertools.permutations(nums))
print(permute([1,2,3]))
#print(itertools_permute([1,2,3]))




# # 스택으로 구현
# lst = [1,2,3]
# n = 3

# permutations = []
# stack = [([x], [i]) for i, x in enumerate(lst)]  # 순열저장리스트, 인덱스리스트
# print('초기상태 스택 :', stack)

# while stack:
#     print(stack)
#     per, idx_list = stack.pop()
    
#     # n개를 모두 뽑은 경우 순열을 추가한 후 continue
#     if len(per)==n:
#         permutations.append(per)
#         continue
        
#     # n개를 뽑지않은경우
#     for i in range(len(lst)):
#         # 뽑은 인덱스리스트에 포함되지 않은 경우 추가
#         if i not in idx_list:
#             stack.append((per+[lst[i]], idx_list+[i]))

print('만들어진 순열리스트')
print(permute([1,2,3]))