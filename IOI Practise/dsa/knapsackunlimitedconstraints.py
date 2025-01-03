mw = 20 #max weight
mc = [2,2,0] #max count of each item
w = [1,5,8] #weight of each item
v = [1, 10, 13] #value of each item

dec_first = lambda vec: [vec[0] - 1] + vec[1:] 

def knapsack(mw, w, v, mc=([float("inf")] * len(w))):
    if mw == 0 or w == []:
        return 0
    if mw < w[0] or mc[0] == 0:
        return knapsack(mw, w[1:], v[1:], mc[1:])
    # max of including and moving on, including and not moving on, not including
    return max([knapsack(mw - w[0], w[1:], v[1:], mc[1:]) + v[0], knapsack(mw - w[0], w, v, dec_first(mc)) + v[0], knapsack(mw, w[1:], v[1:], mc[1:])])

print(knapsack(mw,w,v, mc))