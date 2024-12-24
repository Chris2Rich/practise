s = input()
tri = [s]
for i in range(len(s) -1):
    t = ""
    for j in range(len(tri[-1])-1):
        if tri[-1][j] == tri[-1][j+1]:
            t += tri[-1][j]
        elif set([tri[-1][j], tri[-1][j+1]]) == set(["R", "B"]):
            t += "G"
        elif set([tri[-1][j], tri[-1][j+1]]) == set(["G", "B"]):
            t += "R"
        elif set([tri[-1][j], tri[-1][j+1]]) == set(["R", "G"]):
            t += "B"
    tri.append(t)

print(tri[-1][0])