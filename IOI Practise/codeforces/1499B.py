res = []
for i in range(int(input())):
    inp = input()
    z = inp.rfind("00")
    o = inp.find("11")
    if z != -1 and o != -1:
        if z > o:
            res.append("No")
        else:
            res.append("Yes")
    else:
        res.append("Yes")
for i in res: print(i)