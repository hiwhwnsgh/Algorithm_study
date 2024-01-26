import sys
import collections
from string import ascii_uppercase

alphabet = list(ascii_uppercase)
dic = collections.defaultdict(int)
value = 1
for i in alphabet:
    dic[i]= value
    value+=1
array = list(sys.stdin.readline().rstrip())
count = 1
result = dic[array.pop()]

for i in range(len(array)):
    v = array.pop()
    result +=  26 * count * dic[v]
    count *= 26
print(result)

# s = input()
# e = len(s) - 1
# a = 0
# for i in s:
#     a += (26 ** e) * (ord(i) - 64)
#     e -= 1
# print(a)