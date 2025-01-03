w = [1, -1, 1]
v = [1, -1, 100]
s = 1

def solve(n,s,v):
    if s == 0 or n == []:
        return 0
    if s < n[0]:
        return solve(n[1:], s, v[1:])
    return max(solve(n[1:], s, v[1:]), solve(n[1:], s-n[0], v[1:]) + v[0])

print(solve(n,s,v))