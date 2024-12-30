inp = [int(i) for i in input()]
targ = [i+1 for i in range(7)]

op1 = lambda v : v[1:4] + [v[0]] + v[4:8]
op2 = lambda v : v[0:3] + [v[-1]] + v[3:6]
op3 = lambda v : [v[3]] + v[0:3] + v[4:8]
op4 = lambda v : v[0:3] + v[4:8] + [v[3]]

def solve():
    if inp == targ:
        print(0)
        return

    memo = {}
    q = [(inp, 1)]
    hist = 1
    while True:
        vt, depth = q.pop(0)
        if str(vt) not in memo:
            res = [op1(vt),op2(vt),op3(vt),op4(vt)]
            if targ in res:
                print(depth)
                return
            q += [(i, depth+1)for i in res]
            memo.update({str(vt): depth})
        hist += 4

solve()