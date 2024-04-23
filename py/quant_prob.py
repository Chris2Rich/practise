# Recursion as solution to number of trials for discrete memoryless random function to return same value 1/px times
px = 1/3

dp = []
def prob(n):
    if n == 1:
        return int(1/px)
    else:
        if len(dp) < n:
            dp.append(int(prob(n-1) + 1/(px ** n)))
        return dp[n-2]
        
print(prob(1))
