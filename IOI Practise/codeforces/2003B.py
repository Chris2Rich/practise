ans = []
for i in range(int(input())):
    input()
    v = [int(i) for i in input().split()]
    v.sort()
    a = 0
    b = len(v)
    res = 0
    while a <= b:
        res = v[a]
        a += 1
        b -= 1
    ans.append(res)
for i in ans: print(i)