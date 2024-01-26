alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string = input()
total = 0
for i in range(len(string)):
    if string[i] in ['A','B','C']:
        total+=2
    elif string[i] in ['D','E','F']:
        total+=3
    elif string[i] in ['G','H','I']:
        total+=4
    elif string[i] in ['J','K','L']:
        total+=5
    elif string[i] in ['M','N','O']:
        total+=6
    elif string[i] in ['P','Q','R','S']:
        total+=7
    elif string[i] in ['T','U','V']:
        total+=8
    else:
        total+=9
total += len(string)
print(total)
