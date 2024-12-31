n, k = [int(i) for i in input().split()]
v = [1 if i == "a" else 0 for i in input()]

# longest subarray with at most k abberations
# max nlogn time

# n^2 time solution
def solve():
    cheat = sum(v)
    if cheat + k >= n or cheat - k <= 0:
        return n

    def mod_kadane(v,t):
        if v == []:
            return 0
        res = 0
        curr = 0
        opp = 0
        test = []
        for i in range(len(v)):
            if v[i] != t:
                test.append(i)
                opp += 1
                if opp > k:
                    opp = 0
                    curr = 0
            else:
                curr += 1
                res = max(curr, res)
        return res + k

    return max(max([mod_kadane(v[i:],1) if v[i] else 0 for i in range(n)]), max([mod_kadane(v[i:],0) if not v[i] else 0 for i in range(n)]))
print(solve())