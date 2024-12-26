n = int(input())
r = int(input())
v = [i+1 for i in range(0,n)]
i = 1
ptr = 0
while len(v) > 1:
    if ptr >= len(v):
        ptr -= len(v)
    if i % r == 0 and i != 0:
        del v[ptr]
        ptr -= 1
    i += 1
    ptr += 1
print(v[0])