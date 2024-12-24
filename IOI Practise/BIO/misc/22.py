def turing(s):
    res = s[0]
    for i in range(1, len(s)):
        index = ord(s[i]) - ord(s[i-1])
        if index <= 0:
            index += 26
        index += 64
        res += chr(index)
    return res

