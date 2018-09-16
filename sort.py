from random import randint

d = {x: randint(60, 100) for x in 'abcxyz'}

# print(sorted(d))


# print(list(iter(d)))

# print(list(zip(d.values(), d.keys())))

# print(sorted(list(zip(d.values(), d.keys()))))

print(sorted(d.items(), key=lambda x: x[1]))
