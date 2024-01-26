import string
N,B= input().split()
B = int(B)

def convert_to(N,B):
    alphabet = "0123456789"+string.ascii_uppercase
    multiplier,result = 1, 0
    for i in N[::-1]:
        num = alphabet.index(i)
        result += num % B * multiplier
        multiplier *= B
        
    return result

print(convert_to(N,B))

