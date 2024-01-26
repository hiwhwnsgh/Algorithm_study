List = [i for i in range(1,10001)]
l=[]
for i in range(1,10001):
    num = i
    total = i
    while(num>=10):
        total += num%10
        num = int(num/10)
    total += num %10
    l.append(total)
self_number = [x for x in List if x not in l]
self_number.sort()
for i in range(len(self_number)):
    print(self_number[i])
