res = []
for i in range(int(input())):
    n,k = [int(i) for i in input().split()]
    v = []
    for i in range(n):
        v.append(int(input()))
    res.append("YES" if k >= (min(v) * ((2 * (len(v) - 1) - 1) if len(v) > 1 else 1)) else "NO")
for i in res: print(i)