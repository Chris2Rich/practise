file = open(".\\advent_of_code24\\1.txt", "r")
lines = file.readlines()
file.close()
l1 = [i[0:5] for i in lines]
l2 = [i[8:13] for i in lines]

l1.sort()
l2.sort()

print(sum([abs(int(l1[i]) - int(l2[i])) for i in range(0, len(l1))]))