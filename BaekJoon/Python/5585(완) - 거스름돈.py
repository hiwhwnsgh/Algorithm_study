import sys

price = 1000
dic = {500:0,100:0,50:0,10:0,5:0,1:0}
money = int(sys.stdin.readline())
count = 0
price -= money
for key,value in dic.items():
    count += price // key
    price %= key
print(count)