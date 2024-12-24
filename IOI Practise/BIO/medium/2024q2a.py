import math
s, v = #input().split()

e = lambda x: int(2 * (x))
o = lambda x: int(2 * (x) - 1)
t = lambda x: int((pow(8*(x+1) - 7, 0.5)-1)// 2 + 1)
funcs = {"E": e, "O": o, "T": t}
compose = lambda f1, f2: lambda x: f2(f1(f2(x)))

def parse(start=0):
    lhs = None
    for i in range(start, len(s)):
        rhs = None
        if s[i] == ")":
            return lhs
        elif s[i] == "(":
            rhs = parse(start=i+1)
        else:
            if lhs == None:
                lhs = funcs[s[i]]
            else:
                rhs = funcs[s[i]]
                lhs = compose(lhs, rhs)
    return lhs

print(parse()(int(v)))