memo = {1:1}

def solve(n, max_el=0):
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1
    if n in memo:
        return memo[n]
    
    if max_el == 0:
        max_el = n

    sol = 0
    for i in range(1, min(n+1, max_el + 1)):
        sol += solve(n-i, i)

    memo.update({n: sol})
    return sol

solve(4)
print(memo)