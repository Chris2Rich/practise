# Recursion as solution to number of trials for discrete memoryless random function to return same value 1/px times
px = 1/2

def prob(n):
    if n == 1:
        return 1/px
    else:
        return prob(n-1) + 1/(px ** n)
        
print(prob(5))
