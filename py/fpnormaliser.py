mantissa = 4
exponent = 4

def dectofixbin(x: int) -> str:
    s = ""
    exp = 0

    if x > 0:
        while 2 ** exp < x:
            exp += 1
        
        l = exp

        while x != 0:
            if x - 2**exp >= 0:
                s += "1"
                x -= 2**exp
            else:
                s += "0"
            exp -= 1
            if exp == -1:
                s += "."
        if len(s) < l:
            s += "0" * (l + 1 - len(s))
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

def dectofp(x: int) -> str:
    mnt = dectofixbin(x).replace(".", "")
    exp = dectofixbin(dectofixbin(x).find(".")).replace(".", "")

    if len(exp) > exponent:
        return FloatingPointError()
    
    if exp[0] == 1:
        exp = ("1" * exponent + exp)[len(exp):]
    else:
        exp = ("0" * exponent + exp)[len(exp):]

    mnt = (mnt + "0" * mantissa)[:mantissa]

    return mnt , exp

print(dectofp(1.25))