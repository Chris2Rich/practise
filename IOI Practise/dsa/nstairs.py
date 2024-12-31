n = 5
memo = {}
def solve(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    memo.update({n : solve(n-1) + solve(n-2)})
    return memo[n]

print(solve(234))