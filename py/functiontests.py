import timeit as tm
import time

def add1(x):
    return x+1

#print(tm.timeit(stmt=lambda:add1,number=100))

def printn(n):
    print(str([i for i in range(n)])[1:-1])
    return None

def printstars(n):
    a = ""
    for i in range(1,n+1):
        a += str("*" * i) + str(i) + "\n"
    for i in range(1,n):
        a += str("*" * (n-i)) + str(n-i) + "\n"
    return a
    
def printcube(n):
    for i in range(0, n):
        for j in range(0, n):
            print("*", end="")
        print(" ",i+1)

def printwave(n):
    for i in range(1, n+1):
        print(str(i)*i, end="")
        print(" "*n, i)
    for i in range(1, n):
        print(str(n-i)*(n-i), end="")
        print(" "*n, (n-i))
    for i in range(0, n):
        print(str(n-i)*(n-i), end="")
        print(" "*n, (n-i))
    for i in range(2, n+1):
        print(str(i)*i, end="")
        print(" "*n, i)

printwave(1)