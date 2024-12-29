memo = {}
def fib(n):
    if n < 0:
        return -1
    if n in memo:
        return memo[n]
    else:
        if n < 2:
            memo.update({n: 1})
            return memo[n]
        else:
            if n-1 in memo:
                memo.update({n: memo[n - 1] + memo[n - 2]})
                return memo[n]
            else:
                memo.update({n: fib(n-1) + fib(n-2)})
                return memo[n]
    return -1

print(fib(int(input())))