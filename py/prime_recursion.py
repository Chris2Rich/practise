def recursive_prime(n, indx=None):
    if indx == None:
        indx = int(pow(n, 0.5)) + 1
    if indx == 1:
        return True
    if n % indx == 0:
        return False
    return recursive_prime(n, indx-1)

print(recursive_prime(7))

def maxv(v, mx=None):
    if v == []:
        return mx
    if mx == None:
        mx = v[0]
    mx = max(v[0], mx)
    return maxv(v[1:], mx)

print(maxv([3,1,1,2,0]))