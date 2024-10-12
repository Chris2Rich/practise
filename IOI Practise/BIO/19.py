def palcheck(s):
    return s == s[::-1]

def q1(n):
    tmp = n + 1
    while(not palcheck(str(tmp))):
        tmp += 1
    return tmp

def q1c():
    t = set([(lambda x: x if palcheck(str(x)) else 0)(i) for i in range(0, 100000)])
    res = 0
    for i in range(0, 100000):
        for j in t:
            if i - j in t:
                res += 1
                break

    return 100000 - res

def q3(n, head):
    res = 0
    possible = [chr(i) if chr(i) not in head else None for i in range(65, 65 + n)]

    return possible

print(q3(4, "CB"))