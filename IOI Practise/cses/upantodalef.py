input()
n = [int(i) for i in input().split()]

def solve():
    m = 0
    if len(n) == 1:
        print("0")
        return
    for i in range(1, len(n)):
        if n[i] < n[i-1]:
            m += n[i-1] - n[i]
            n[i] = n[i-1]
    print(m)

solve()