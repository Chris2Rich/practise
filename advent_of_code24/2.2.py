file = open("./advent_of_code24/2.txt", "r")
lines = file.readlines()
file.close()

def check_permutation(v):
    incr = False
    safe = True
    if v[1] - v[0] > 0:
        incr = True
    if incr:
        for j in range(0, len(v) - 1):
            if v[j + 1] - v[j] <= 0:
                safe = False
                break
            if v[j + 1] - v[j] > 3:
                safe = False
                break
    else:
        for j in range(0, len(v) - 1):
            if v[j] - v[j + 1] <= 0:
                safe = False
                break
            if v[j] - v[j + 1] > 3:
                safe = False
                break
    return int(safe)

res = []

for i in lines:
    v = i.split(" ")
    v = [int(j) for j in v]
    res.append(int(sum([check_permutation(i) for i in [v[0:j] + v[j+1:] for j in range(0, len(v))]]) > 0))

print(sum(res))