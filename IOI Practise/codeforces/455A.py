input()
nums = [int(i) for i in input().split()]
res = 0

s = set(nums)
ma = max(s)
mi = min(s)

scores = {i: nums.count(i) * i for i in s}
cost = [[
    i,
    scores[i+1] - scores[i] if i == mi else
    scores[i-1] - scores[i] if i == ma else
    (scores[i+1] + scores[i-1]) - scores[i]
    ] for i in s
]

# select minimum cost, add score, remove adjacent costs
while len(scores) != 0:
    indx = {cost[i][0]: i for i in range(0, len(cost))}
    tmp = min(cost, key= lambda x: x[1])
    res += scores[tmp[0]]
    if tmp[0] + 1 in scores:
        if tmp[0] + 2 in scores:
            cost[indx[tmp[0] + 2]][1] -= scores[tmp[0] + 1]
        del cost[indx[tmp[0] + 1]]
        del scores[tmp[0] + 1]
    if tmp[0] - 1 in scores:
        if tmp[0] - 2 in scores:
            cost[indx[tmp[0] - 2]][1] -= scores[tmp[0] - 1]
        del cost[indx[tmp[0] - 1]]
        del scores[tmp[0] - 1]
        indx[tmp[0]] -= 1

    del cost[indx[tmp[0]]]
    del scores[tmp[0]]

print(res)