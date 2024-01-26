import sys
global count
count =0
global list_print
list_print = []
def hanoi_tower(n,first,two,third):
    if N<=20:
        global count
        global list_print
        count +=1
        if n==1:
            list_print.append(first+' '+third)
        else:
            hanoi_tower(n-1,first,third,two)
            list_print.append(first+' '+third)
            hanoi_tower(n-1,two,first,third)
    
N = int(sys.stdin.readline())
hanoi_tower(N,'1','2','3')
print(count)
for i in list_print:
    print(i)
