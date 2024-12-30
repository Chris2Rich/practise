w = input()
v = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
ans = ""
for i in v:
    solved = True
    wa = w
    for j in i:
        res = wa.find(j)
        if res != -1:
            wa = wa[res:]
        else:
            solved = False
            break
    if solved:
        ans = i

print({v[i]: i+1 for i in range(len(v))}[ans] if ans != "" else "NO")