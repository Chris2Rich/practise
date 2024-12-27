tests = int(input())
res = []
for i in range(tests):
    input()
    s = input()
    res.append(sum([s[:i][0] != s[i:][-1] and s[:i][-1] != s[i:][0] for i in range(1, len(s))]) > 0)
for i in res: print("yes" if i else "no")