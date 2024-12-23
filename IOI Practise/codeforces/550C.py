n = "00" + input()

def solve():
    div = False
    for i in [str(i) if i > 100 else "0" + str(i) if i > 10 else "00" + str(i) for i in range(0, 1000, 8)]:
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

solve()