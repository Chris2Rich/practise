n = int(input())

def solve():
    if n == 2 or n == 3:
        return "NO SOLUTION"
    return " ".join([str(i) for i in range(2, n+1, 2)]) + " " + " ".join([str(i) for i in range(1, n+1, 2)])

print(solve())