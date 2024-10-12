n = 105000
nums = [[i, 0] for i in range(0, n + 1)]
for i in nums:
    if(i[0] >= 2):
        if i[1] == 0:
            for j in range((i[0] * 2), n + 1, i[0]):
                nums[j][1] = 1
primes = [i for i in filter(lambda x: True if x != None else False, [i[0] if(i[1] == 0) else None for i in nums][2:])]
print(primes[10000])