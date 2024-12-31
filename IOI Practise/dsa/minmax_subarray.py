import random
v = [random.randint(-1000,1000) for i in range(1000000)]
def max_sub(v):
    curr_val = 0
    max_val = 0
    for i in v:
        curr_val = max(curr_val + i, curr_val)
        max_val = max(curr_val, max_val)
    return max_val

def min_max(v):
    return min([max_sub(v[i:]) for i in range(len(v))])

print(v)
print(max_sub(v))