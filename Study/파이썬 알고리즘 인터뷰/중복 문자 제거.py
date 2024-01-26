

import collections
# 재귀를 이용한 분리
def removeDuplicateLetters(s: str) -> str:
    # 집합으로 정렬
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        # 전체 집합과 접미사 집합이 일치할 때 분리 진행
        if set(s) == set(suffix):
            return char + removeDuplicateLetters(suffix.replace(char,''))
    return ''
# 스택을 이용한 분리
def removeDuplicateLettersStack(s:str) ->str:
    counter, seen, stack = collections.Counter(s), set(), []
    print(counter)
    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    print(stack)
    return ''.join(stack)
        
array = removeDuplicateLetters('bcabc')
stack = removeDuplicateLettersStack('cbacdcbc')
#print(array)
print(stack)