from random import randint;

data = {x: randint(60, 100) for x in range(1, 21)}

print(data)

data = {k: v for k, v in data.items() if v > 90}

print(data)

data = [randint(-10, 10) for _ in range(10)]

s = set(data)

s = {i for i in s if i % 3 == 0}

print(s)
