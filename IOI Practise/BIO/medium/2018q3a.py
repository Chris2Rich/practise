input()
s = input()

def between(v):
    if v[1] > v[0] > v[2] or v[2] > v[0] > v[1]: return "s"
    if v[0] > v[2] > v[1] or v[1] > v[2] > v[0]: return "p"
    return None

memo = {s:[]}
q = [s]
def solve(s):
    global q
    res = [between(s[i:]) for i in range(len(s)-2)]
    res = list(filter(lambda x: x != None, [(s[i+1:i+3], i+1) if res[i] == "s" else (s[i:i+2], i) if res[i] == "p" else None for i in range(len(res))]))
    new = []
    for i in res:
        tmp = list(s)
        tmp[i[1]:i[1]+2] = i[0][::-1]
        tmp = "".join(tmp)
        if tmp not in memo:
            memo.update({tmp: []})
            memo[s].append(tmp)
            new.append(tmp)

    q += new
    if q == []: return
    return solve(q.pop(0))

solve(s)

distances = {i:float("inf") for i in (memo)}
distances[s] = 0
def dfs(s, score=1):
    for i in memo[s]:
        distances[i] = min(distances[i], score)
        dfs(i, score+1)
    return
dfs(s)
print(distances[max(distances, key=lambda x: distances[x])])