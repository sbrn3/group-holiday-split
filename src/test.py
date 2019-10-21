from itertools import product

test = [1, 2, 3, 4]

x = list(product(test, repeat=10))
print(len(x))
for i in range(10):
    print(x[i])