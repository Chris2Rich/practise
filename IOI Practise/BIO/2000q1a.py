s = input()
def solve():
    for i in range(0, len(s)+1):
        for j in range(i, len(s)+1):
            if s[i:j] != "":
                m = (i - j) // 2
                if s[i:j][:m] == s[i:j][m:]:
                    return False
    return True
print("Accepted" if solve() else "Rejected")