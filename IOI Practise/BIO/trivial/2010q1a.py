n = int(input())
anagram = lambda a,b: {i: str(a).count(i) for i in str(a)} == {i: str(b).count(i) for i in str(b)}
res = [anagram(w, w*i) for i in range(2,10) for w in [n]]
if sum(res) == 0:
    print("NO")
else:
    s = ""
    for i in range(0, len(res)):
        if res[i]:
            s += str(i+2) + " "
    print(s)