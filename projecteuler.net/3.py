m = 600851475143
n = int(600851475143 ** 0.5 // 1 + 1)
nums = [[i, 0] for i in range(0, n + 1)]
for i in nums:
    if(i[0] >= 2):
        if i[1] == 0:
            for j in range((i[0] * 2), n + 1, i[0]):
                nums[j][1] = 1

primes = filter(lambda x: True if x != None else False, [i[0] if(i[1] == 0) else None for i in nums][:1:-1])
for i in primes:
    if(m % i == 0):
        print(i)
        break