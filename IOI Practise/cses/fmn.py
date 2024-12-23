input()
n = [int(i) for i in input().split()]
n.sort()
m = 1
for i in n:
    if i == m:
        m += 1

print(m)