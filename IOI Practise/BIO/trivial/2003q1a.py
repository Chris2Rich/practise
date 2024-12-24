s = input()
sum = 0
qpos = 0
for i in range(0, len(s)):
    if s[i] != "?" and s[i] != "X":
        sum += (len(s) - i) * int(s[i])
    elif s[i] == "X":
        sum += 10
    else:
        qpos = len(s) - i

for i in range(0, 11):
    if (sum + (qpos * i)) % 11 == 0:
        if i == 10:
            print("X")
        else:
            print(i)