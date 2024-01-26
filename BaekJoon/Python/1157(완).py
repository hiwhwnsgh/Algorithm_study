S = input()
S = S.lower()
maxinium = 0
asc = 97
string =""
for i in range(26):
    if maxinium < S.count(chr(asc)):
        string = chr(asc)
        maxinium = S.count(chr(asc))
    elif maxinium == S.count(chr(asc)) and string != chr(asc):
        string = "?"
    asc+=1
                           
print(string.upper())
