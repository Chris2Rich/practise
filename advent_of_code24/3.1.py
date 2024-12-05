file = open("./advent_of_code24/3.txt", "r")
lines = file.readlines()
file.close()

s = ""
for i in lines:
    s += i

import re
matches = [i.group() for i in re.finditer(r"mul\(\d*,\d*\)", s, re.MULTILINE)]
n1 = [re.search(r"(?<=mul\()\d*", i) for i in matches]
n2 = [re.search(r"(?<=\,)\d*", i) for i in matches]
res = [[int(n1[i].group()) * int(n2[i].group()), n1[i].span()[0]] for i in range(0, len(matches))]

dos = [i.span()[0] for i in re.finditer(r"do\(\)", s, re.MULTILINE)]
donts = [i.span()[0] for i in re.finditer(r"don\'t\(\)", s, re.MULTILINE)]

ans = 0
for i in res:
    cdo = 0
    cdont = 0
    for j in dos:
        if j < i[1]:
            cdo = j
    for j in donts:
        if j < i[1]:
            cdont = j
    if cdo < cdont:
        ans += 0
    else:
        ans += i[0]

print(dos, donts)