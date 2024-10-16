words = {3: "Fizz", 5: "Buzz", 7: "Bazz"}
n = 100

for i in range(1, n + 1):
    if not 0 in [i % j for j in words.keys()]:
        print(i)
    else:
        s = ""
        for j in words.keys():
            if i % j == 0:
                s += words[j]
        print(s)
