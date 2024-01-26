a,b = input().split()
string = ""
string2 =""
for i in range(len(a)):
    string += a[-i-1]
    string2 += b[-i-1]
if int(string)<int(string2):
    print(string2)
else:
    print(string)
