n = int(input())
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n < 2:
        memo.update({n: 1})
    else:
        memo.update({n: fib(n-1) + fib(n-2)})
    return memo[n]

fibs = [fib(0)]
res = []
i = 1
while fibs[-1] < n:
    fibs.append(fib(i))
    i += 1

i = -1
while n != 0:
    if fibs[i] <= n:
        n -= fibs[i]
        res.append(fibs[i])
    i -= 1

for i in res: print(i, end=" ")