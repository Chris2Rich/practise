#too slow
s = "BED"
n = 10
m = 1243
grammar = {"A": ["B"], "B": ["A", "B"], "C": ["C", "D"], "D": ["D", "C"], "E": ["E", "E"]}
for i in range(n):
    s = [item for sub in list(map(lambda x: grammar[x], s)) for item in sub]
s = s[:m]
print(s.count("A"), s.count("B"), s.count("C"), s.count("D"), s.count("E"))