n = 5
dp = [[0] * n for i in range(n)]
dp[0][0] = 1
for i in range(0,n):
    for j in range(0,n):
        if i != n - 1:
            dp[i+1][j] += dp[i][j]
        if j != n - 1:
            dp[i][j+1] += dp[i][j]

for i in dp: print(i)