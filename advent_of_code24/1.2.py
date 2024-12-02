file = open(".\\advent_of_code24\\1.txt", "r")
lines = file.readlines()
file.close()
l1 = [i[0:5] for i in lines]
l2 = [i[8:13] for i in lines]

sim = {i: l2.count(i) for i in l1}
print(sum([int(i) * sim[i] for i in l1]))