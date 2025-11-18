def solve_recur(s, k):
    if k == 0:
        return s
    if len(s) == k:
        return ""
    if int(s[0]) < max([int(i) for i in s[:k+1]]):
        return solve_recur(s[1:], k-1)
    return s[0] + solve_recur(s[1:], k)

def solve_iter(s, k):
    res = ""
    while k >= 0:
        if len(s) == k:
            return res
        if int(s[0]) < max([int(i) for i in s[:k+1]]):
            s = s[1:]
            k -= 1
        else:
            res += s[0]
            s = s[1:]
    return res

print([solve_iter("7396350874", i+1) for i in range(10)])
print([solve_recur("7396350874", i+1) for i in range(10)])