s1 = "Lovesasdasufh"
s2 = "Moviesdsafbisdf"

dp = {}
def ed(s1,s2):
    if s1 == "" or s2 == "":
        dp.update({(s1,s2) : len(max(s1,s2,key=len))})
        return dp[(s1,s2)]
    else:
        if s1[0] == s2[0]:
            dp.update({(s1,s2) : ed(s1[1:], s2[1:])})
            return dp[(s1,s2)]
        else:
            dp.update({(s1,s2) : 1 + min(ed(s1[1:], s2),ed(s1,s2[1:]),ed(s1[1:],s2[1:]))})
            return dp[(s1,s2)]

print(ed(s1,s2))