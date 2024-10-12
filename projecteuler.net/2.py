phi = (1 + (5 ** 0.5)) / 2

def fib(n):
    return int(((phi ** n) - ((-phi) ** -n)) / (5 ** 0.5))

n = 0
vals = []
while(fib(n) < 4000000):
    if(fib(n) % 2 == 0):
        vals.append(fib(n))
    n += 1

print(sum(vals))