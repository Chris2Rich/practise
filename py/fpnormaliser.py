nummantissa = 10
numexp = 6

def dectofixbin(x: int) -> str:
    s = ""
    exp = 0

    if x > 0:
        while 2 ** exp < x:
            exp += 1
        
        while x != 0:
            if exp == -1:
                s += "."
            if x - 2**exp >= 0:
                s += "1"
                x -= 2**exp
            else:
                s += "0"
            exp -= 1
        return s
    if x == 0:
        return "0"
    if x < 0:
        s = dectofixbin(-x)
        s = "".join(["0" if i == "1" else "1" if i == "0" else "." for i in s])

        if s[-1] == "0":
            s = s[:-1] + "1"
        else:
            s = s[: s.rfind("0")] + "".join(["0" if i == "1" else "1" if i == "0" else "." for i in s[s.rfind("0"): ]])

        return s
    return None, None

print(dectofixbin(-23.5))