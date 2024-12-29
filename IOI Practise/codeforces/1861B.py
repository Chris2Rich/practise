res = []
for i in range(int(input())):
    a = input()
    b = input()
    res.append("yes" if True in [a[i] == b[i] == "0" and a[i+1] == b[i+1] == "1" for i in range(len(a)-1)] else "no")
for i in res: print(i)