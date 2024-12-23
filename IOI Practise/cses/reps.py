s = input()
m = 1
t = 1
for i in range(0, len(s) - 1):
    if s[i] == s[i+1]:
        t += 1
        m = max(m, t)
    else:
        t = 1
print(m)