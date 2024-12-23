s = input()
def solve():
    p1 = set()
    p2 = set()

    for i in range(0, len(s) - 1):
        if s[i] + s[i+1] == "AB":
            p1.add(i)
        if s[i] + s[i+1] == "BA":
            p2.add(i)

    print(p1, p2)

    if len(p1) == 0 or len(p2) == 0:
        print("NO")
        return

    mat = []
    for i in p1:
        mat.append([])
        for j in p2:
            mat[-1].append(abs(i -j))

    for i in range(0, len(mat)):
        mat[i] = [i for i in filter(lambda x: x if x > 1 else None, mat[i])]

    for i in mat:
        if len(i) != 0:
            print("YES")
            return

    print("NO")
    return

solve()