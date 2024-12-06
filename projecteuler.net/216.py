#Generate list of primes

n = 10 ** 4

nums = [(2 * (i**2)) - 1 for i in range(2, int(pow((n + 1) / 2, 1/2)) + 1)]
marked = set()

for i in nums:
    if i not in marked:
        for j in range(2*i, len(nums) + 2, i):
            marked.add(nums[j-2])

primes = [i for i in filter(None, [i if i not in marked else None for i in nums])]
print(len(primes))