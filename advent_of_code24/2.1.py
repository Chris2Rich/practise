file = open(".\\advent_of_code24\\2.txt", "r")
lines = file.readlines()
file.close()

res = []

for i in lines:
    v = i.split("")
    v = [int(j) for i in v]
    incr = False
    if v[1] - v[0] > 0:
        incr == True
    if incr:
        for j in range(0, len(v) - 1):
            if v[j + 1] - v[j] <= 0:
                res.append(0)
                break
            if v[j + 1] - v[j] > 3:
                res.append(0)
                break
    else:
        for j in range(0, len(v) - 1):
            if v[j] - v[j + 1] <= 0:
                res.append(0)
                break
            if v[j] - v[j + 1] > 3:
                res.append(0)
                break
    res.append(1)

print(sum(res))