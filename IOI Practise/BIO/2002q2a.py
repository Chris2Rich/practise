solve = {"pa": "1", "re": "2", "ci": "3", "vo": "4", "mu": "5", "xa": "6", "ze": "7", "bi": "8", "so": "9", "no": "0"}
print("".join([solve[i] for i in (lambda x: [x[i] + x[i+1] for i in range(0, len(x), 2)])([i for i in input()])]))