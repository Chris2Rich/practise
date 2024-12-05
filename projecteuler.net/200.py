#Generate list of primes
#Create sorted list of squbes
#filter for those with 200
#check if prime-proof

nums = [i for i in range(2, 2024)]
marked = set()

for i in nums:
    if i not in marked:
        for j in range(2*i, len(nums) + 2, i):
            marked.add(nums[j-2])

primes = [i for i in filter(None, [i if i not in marked else None for i in nums])]
print(primes)