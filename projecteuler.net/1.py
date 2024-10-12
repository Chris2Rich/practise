multis_3 = [i for i in filter(lambda x: None if x % 3 else x, range(0, 1000))]
multis_5 = [i for i in filter(lambda x: None if x % 5 else x, range(0, 1000))]
print(sum(set(multis_3 + multis_5)))