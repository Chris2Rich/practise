s = input()
def solve():
    p1 = set()
    p2 = set()

    for i in range(0, len(s) - 1):
        if s[i] + s[i+1] == "AB":
            p1.add(i)
        if s[i] + s[i+1] == "BA":
            p2.add(i)

    for i in p1:
        for j in p2:
            if abs(i -j) > 1:
                print("YES")
                return

    print("NO")
    return

solve()