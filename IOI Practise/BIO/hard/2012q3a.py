n = 1000
init = {"0": "ZERO", "1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR", "5": "FIVE", "6": "SIX", "7": "SEVEN", "8": "EIGHT", "9": "NINE"}
comp = lambda x, y : sum({i : abs(x[i] - y[i]) for i in x}.values()) <= 5
nums = [{i: "".join([init[l] for l in str(k)]).count(i) for i in [chr(j) for j in range(65, 91)]} for k in range(n)]
mat = [[j if comp(nums[i], nums[j]) and i != j else None for j in range(n)] for i in range(n)]

def bfs(a,b):
        q = [(a, 0)]
        seen = set()
        while q != []:
            v = q.pop(0)
            if v[0] == b:
                print(v[1])
                return
            if v[0] not in seen:
                seen.add(v[0])
                for i in mat[v[0]]:
                    if i != None and i not in seen:
                        if i == b:
                            print(v[1] + 1)
                            return
                        q.append((i, v[1] + 1))
            else:
                continue

a,b = [int(i) for i in input().split()]
c,d = [int(i) for i in input().split()]
e,f = [int(i) for i in input().split()]

bfs(a,b)
bfs(c,d)
bfs(e,f)