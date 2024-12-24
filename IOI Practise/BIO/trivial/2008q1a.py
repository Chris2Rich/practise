n = int(input())
primes = [2]
for i in range(3, n):
    flag = True
    for j in range(0, len(primes)):
        if primes[j] > pow(i, 0.5):
            break
        else:
            if i % primes[j] == 0:
                flag = False
    if flag == True:
        primes.append(i)
    
c = 0
for i in range(0, len(primes)):
    for j in range(i, len(primes)):
        if primes[i]+primes[j] == n:
            c += 1

print(c)