L = 15

c = 0
for x in range(2, L):
    for y in range(x+1, L+1):
        if x & 1 == 1 and y & 1 == 1:
            continue
        n2 = (x * y) / (x + y)
        if(n2 == int(n2)):
            print(x, y, n2)
            c += 1

print(c)
#TOO SLOW!