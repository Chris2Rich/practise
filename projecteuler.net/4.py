def pali(n):
    return str(n) == str(n)[::-1]

def q4():
    m = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if(pali(i * j)):
                m = max(i * j, m)
    print(m)
q4()