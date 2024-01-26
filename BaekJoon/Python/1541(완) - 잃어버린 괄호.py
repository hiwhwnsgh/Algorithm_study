import sys
"""
내가 푼 방법
N = sys.stdin.readline()

array = []
start = 0
count = 0
check = True
for i in range(len(N)):
    if N[i] in "-+\n":
        if N[i] == '-':
            count+=2
        array.append(int(N[start:i]))
        array.append(N[i])
        start = i+1
for i in range(len(array)+count):
    if array[i] == "-" and check:
        array.insert(i+1,'(')
        check = False
    elif array[i] == "-" or array[i] == '\n' and not check:
        check = True
        array.insert(i,')')
        if array[i] == '\n':
            break
    array[i] = str(array[i])
result = ''.join(array)
total = eval(result)
print(total)
"""
# 더 좋은 인터넷 방법
# '-' 단위로 분리 이문장이 핵심!! '-'글자가 나온다면 그 다음 문자들 '-','+'든 모두 다 음수처리
a = input().split('-')  
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):    # 0번째인덱스는 무조건 양수이므로 첫번째 인덱스부터 검색
    n -= num[i]
print(n)