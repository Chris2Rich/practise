s = [2,6,4,1,2,2,7]
scan = [sum(s[:i+1]) % len(s) for i in range(len(s))]
for i in range(len(s)):
    if scan[i] == 0:
        print(s[:i+1])

for i in range(len(s)-1):
    for j in range(i+1, len(s)):
        if scan[i] == scan[j]:
            print(s[i+1:j+1])