n = 18
w = [1,5,8]
v = [1, 10, 13]

def knapsack(n, w, v):
    if n == 0 or w == []:
        return 0
    if n < w[0]:
        return knapsack(n, w[1:], v[1:])
    # max of including and moving on, including and not moving on, not including
    return max([knapsack(n - w[0], w[1:], v[1:]) + v[0], knapsack(n - w[0], w, v) + v[0], knapsack(n, w[1:], v[1:])])

print(knapsack(n,w,v))