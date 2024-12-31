import math
s, v = input().split()

e = lambda x: int(2 * (x))
o = lambda x: int(2 * (x) - 1)
t = lambda x: int(math.floor(pow(2*x, 0.5) + 0.5))
funcs = {"E": e, "O": o, "T": t}
compose = lambda f1, f2: lambda x: f2(f1(f2(x))) if type(f1) != list and type(f2) != list else f2[0](f1[0](f2[0](x))) if type(f1) == list and type(f2) == list else f2(f1[0](f2(x))) if type(f2) != list else f2[0](f1(f2[0](x)))

s = list(filter(lambda x: x != [], [list(filter(lambda x: x != [], [[k for k in j] for j in i.split(")")])) for i in s.split("(")]))
for j in s:
    for i in j:
        i[0] = funcs[i[0]]
        while len(i) != 1:
            if type(i[0]) == str:
                i[0] = funcs[i[0]]
            if type(i[1]) == str:
                i[1] = funcs[i[1]]
            i[0] = compose(i[0], i[1])
            del i[1]
    while len(j) != 1:
        j[0] = compose(j[0], j[1])
        del j[1]

tmp = []
for i in s:
    if type(i[0]) == list:
        tmp.append(i[0][0])
    else:
        tmp.append(i[0])
s = tmp

while len(s) != 1:
    s[0] = compose(s[0], s[1])
    del s[1]

print(s[0](int(v)))