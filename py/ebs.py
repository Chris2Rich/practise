def exp(x, n):
    if n == 0:
        return 1
    if n < 0:
        return exp(1 / x, -n)
    if n % 2:
        return x * exp(x*x, (n-1)//2)
    else:
        return exp(x*x, n // 2)

print(exp(2,-3))