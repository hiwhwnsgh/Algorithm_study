
def hammingDistance(x:int,y:int)-> int:
    return bin(x ^ y).count('1')
x=1
y=4
result = hammingDistance(x,y)
print(result)