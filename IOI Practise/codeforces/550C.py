n = input()

dig2 = [str(i) if i > 10 else "0" + str(i) for i in range(0, 100, 8)]
dig3 = [str(i) if i > 100 else "0" + str(i) if i > 10 else "00" + str(i) for i in range(0, 1000, 8)]

def wun():
    if n == "0" or n == "8":
        print("YES")
        print(n)
    else:
        print("NO")

def tu():
    if n in dig2:
        print("YES")
        print(n)
        return

    if "0" in n or "8" in n:
        if n.find("0") != -1:
            print("YES")
            print("0")
        else:
            print("Yes")
            print("8")
    else:
        print("NO")

def trey():
    div = False
    for i in dig3:
        ix = []
        for j in i:
            if ix == []:
                ix.append(n.find(j))
            else:
                ix.append(n.find(j,ix[-1]+1))
        if (ix[0] < ix[1] and ix[1] < ix[2]) and (ix[0] != -1 and ix[1] != -1 and ix[2] != -1):
            div = True
            print("YES")
            if i == "000":
                print("0")
            else:
                print(i.lstrip("0"))
            return
    if div == False:
        print("NO")

if len(n) == 1:
    wun()
if len(n) == 2:
    tu()
if len(n) >= 3:
    trey()