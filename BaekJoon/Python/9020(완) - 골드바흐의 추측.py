import enum
import sys
import math
array = []
dic_array= {}
for j in range(2,10001):
    tf = True
    for i in range(2,int(math.sqrt(j))+1):
        if j % i == 0:
            tf = False
            break
    if tf:
        array.append(j)
for i,n in enumerate(array):
    dic_array[n] = i
N = int(sys.stdin.readline())
for i in range(N):
    min_number = 10001
    result = list(range(2))
    num = int(sys.stdin.readline())
    for i in range(2,num//2+1):
        num_miner = num - i
        if i in dic_array and num_miner in dic_array and abs(num_miner-i) <min_number:
            result[0] = i
            result[1] = num_miner
            min_number = num_miner-i
            
    print(f"{result[0]} {result[1]}")
