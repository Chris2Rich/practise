res = [int(input())]
while res[-1] != 1:
    if res[-1] & 1 == 1:
        res.append(res[-1] * 3 + 1)
    else:
        res.append(res[-1] // 2)
print(" ".join(str(i) for i in res))