def q1a():
    q = [100, 101, 2, 1001, 371293, 789774, 999883, 561125, 661229, 10, 20] # int(input())
    def factorize(n):
        if n in res:
            return
        res[n] = set()
        for i in range(2, int(n // 2) + 1):
            if n % i == 0:
                res[n].add(i)
                factorize(i)
        return
    
    for n in q:
        
        res = {}
        factorize(n)
        upf = []
        for i in res:
            if res[i] == set():
                upf.append(i)
        res = 1
        for i in upf:
            res *= i
        print(res)

def q1b():
    j = 1
    ans = []
    def factorize(n):
        if n in res:
            return
        res[n] = set()
        for i in range(2, int(n // 2) + 1):
            if n % i == 0:
                res[n].add(i)
                factorize(i)
        return
    
    while len(ans) != 10:
        res = {}
        factorize(j)
        upf = []
        for i in res:
            if res[i] == set():
                upf.append(i)
        if set(upf) == {2,5}:
            ans.append(j)
        j += 1
    print(ans)

def q1c():
    ans = {}
    q = [i for i in range(1, 10**1)] # 10 ** 6
    def factorize(n):
        if n in res:
            return
        res[n] = set()
        for i in range(2, int(n // 2) + 1):
            if n % i == 0:
                res[n].add(i)
                factorize(i)
        return
    
    for n in q:
        
        res = {}
        factorize(n)
        upf = []
        for i in res:
            if res[i] == set():
                upf.append(i)
        res = 1
        for i in upf:
            res *= i
        if res in ans:
            ans[res] += 1
        else:
            ans[res] = 1
    m = [0, 0]
    for i in ans:
        if ans[i] > m[0]:
            m[0], m[1] = ans[i], i
    print(m[1])