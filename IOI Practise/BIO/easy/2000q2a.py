grid = {(i+1,j+1):0 for i in range(11) for j in range(11)}
ant1 = {"p": [1,1], "d": 1}
ant2 = {"p": [1,1], "d": 1}

#T1,l2,B3,R4

def move_ant(ant):
    if ant["d"] == 1:
        ant["p"] = [ant["p"][0],ant["p"][1]+1]
    if ant["d"] == 3:
        ant["p"] = [ant["p"][0],ant["p"][1]-1]
    if ant["d"] == 2:
        ant["p"] = [ant["p"][0]+1,ant["p"][1]]
    if ant["d"] == 4:
        ant["p"] = [ant["p"][0]-1,ant["p"][1]]

    if ant["p"][0] > 11 or ant["p"][1] > 11 or ant["p"][0] < 1 or ant["p"][1] < 1:
        return None

    if grid[(ant["p"][0], ant["p"][1])]:
        if ant["d"] == 1:
            ant["d"] = 2
        elif ant["d"] == 2:
            ant["d"] = 3
        elif ant["d"] == 3:
            ant["d"] = 4
        elif ant["d"] == 4:
            ant["d"] = 1
    else:
        if ant["d"] == 1:
            ant["d"] = 4
        elif ant["d"] == 2:
            ant["d"] = 1
        elif ant["d"] == 3:
            ant["d"] = 2
        elif ant["d"] == 4:
            ant["d"] = 3

    grid[(ant["p"][0], ant["p"][1])] = int(not grid[(ant["p"][0], ant["p"][1])])
    return ant

def move(ant1,ant2):
    if ant1 != None:
        ant1 = move_ant(ant1)
    if ant2 != None:
        ant2 = move_ant(ant2)
    if ant1 == None and ant2 == None:
        return None
    return 1

def print_grid():
    s = ""
    n = list(grid)[::-1][0][0]
    for i in list(grid)[::-1]:
        if i[0] != n:
            print(s)
            s = ""
            n = i[0]
        s += str("*" if grid[i] else ".")

    if ant1 != None:
        print(ant1["p"][0], ant1["p"][1], "T" if ant1["d"] == 1 else "L" if ant1["d"] == 2 else "B" if ant1["d"] == 3 else "R" if ant1["d"] == 4 else None)
    else:
        print("Removed")
    if ant2 != None:
        print(ant2["p"][0], ant2["p"][1], "T" if ant2["d"] == 1 else "L" if ant2["d"] == 2 else "B" if ant2["d"] == 3 else "R" if ant2["d"] == 4 else None)
    else:
        print("Removed")

def game():
    inp1 = input().split()
    ant1 = {"p": [int(inp1[0]), int(inp1[1])], "d": 1 if inp1[2] == "T" else 2 if inp1[2] == "L" else 3 if inp1[2] == "B" else 4 if inp1[2] == "R" else None}
    inp2 = input().split()
    ant2 = {"p": [int(inp2[0]), int(inp2[1])], "d": 1 if inp2[2] == "T" else 2 if inp2[2] == "L" else 3 if inp2[2] == "B" else 4 if inp2[2] == "R" else None}

ant1 = {"p": [2,1], "d": 1}
ant2 = {"p": [15,15], "d": 4}

print_grid()
move(ant1,ant2)
move(ant1,ant2)
move(ant1,ant2)
print_grid()