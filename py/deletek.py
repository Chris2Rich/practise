def solve(s, k):
    if k == 0:
        return s
    if len(s) == k:
        return ""
    if int(s[0]) < int(s[1]):
        return solve(s[1:], k-1)
    if int(s[0]) < max([int(i) for i in s[:k+1]]):
        return solve(s[1:], k-1)
    return s[0] + solve(s[1:], k)

print([solve("7396350874", i+1) for i in range(10)])