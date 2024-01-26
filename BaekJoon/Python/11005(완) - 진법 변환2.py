
from audioop import mul

import string
N,B = map(int,input().split())
def convert_to_decimal(N,B):
    result = ""
    alphabet = "0123456789"+string.ascii_uppercase
    while N>0:
        digit = N % B
        result = alphabet[digit] + result
        N = N//B
    return result
print(convert_to_decimal(N,B))
