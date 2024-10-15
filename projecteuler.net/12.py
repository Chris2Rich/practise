triangular = lambda x: 0.5 * x * (x+1)
factor_count = lambda x: sum(x % i == 0 for i in range(1, int(x ** 0.5)+ 1)) * 2 - (x ** 0.5 == int(x ** 0.5))

n = 1
a = factor_count(triangular(n))
while a < 500:
    n *= 2
    a = factor_count(triangular(n))

print(n)
