res = []
for i in range(int(input())):
    input()
    n = [int(i) for i in input().split()]
    input()
    m = [int(i) for i in input().split()]
    costn = [sum(n[:i+1]) for i in range(0, len(n))]
    costm = [sum(m[:i+1]) for i in range(0, len(m))]

    res.append(max(0, max(max(costn), 0) + max(max(costm), 0)))
for i in res: print(i)