from random import sample

l = [i for i in range(1, 51)]
for i in range(3):
    res = sample(l, 7)
    print(sorted(res))

