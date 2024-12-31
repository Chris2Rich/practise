s1 = "Neoliberal Tax Policy"
s2 = "Fairness and Freedom Inspiring"

def LCS(X,Y):
    m = len(X)
    n = len(Y)
    
    dp = [[0] * (n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

print(LCS(s1,s2))