s = list(map(lambda x: ord(x) - ord("A"), input()))
s = list(map(lambda x: chr(x + ord("A")), [s[0]] + [(s[i] - s[i-1] - 1) % 26 for i in range(len(s)-1, 0, -1)][::-1]))
print("".join(s))