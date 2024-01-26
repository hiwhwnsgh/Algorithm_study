stack = []
table = {
    ')' : '(',
    '}' : '{',
    ']' : '['
}
s = '()[]{}'
print(table.items())
for char in s:
    if char not in table:
        stack.append(char)
    elif not stack or table[char] != stack.pop():
        print("실패")
