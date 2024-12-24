import math

def pat(s):
    if(len(s) == 1):
        return True
    n = math.ceil(len(s) / 2)
    l = s[:n]
    r = s[n:]
    if(sorted(list(set(l))) < sorted(list(set(r)))):
        return False
    return pat(l[::-1]) and pat(r[::-1])
    
def q1():
    inp = input().split(" ")
    s1 = inp[0]
    s2 = inp[1]
    if(pat(s1)):
        print("YES")
    else:
        print("NO")
        
    if(pat(s2)):
        print("YES")
    else:
        print("NO")

    if(pat(s1 + s2)):
        print("YES")
    else:
        print("NO")

def q2():
    count = 0
    for i in ["A", "B", "C", "D"]:
        for j in ["A", "B", "C", "D"]:
            for k in ["A", "B", "C", "D"]:
                for l in ["A", "B", "C", "D"]:
                    if(len(set([i, j, k, l])) == 4):
                        count += pat(i + j + k + l)
    print(count)

print(pat("BDCA"))