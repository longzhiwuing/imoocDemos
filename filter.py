import timeit
from random import randint;

data = [randint(-10, 10) for _ in range(10)]

print(data)

filter_data = filter(lambda x: x >= 0, data)

print(list(filter_data))

filter_data = [x for x in data if x >= 0]

print(filter_data)

print('=' * 50)

t1 = timeit.Timer('filter(lambda x: x >= 0, data)', setup='from __main__ import data')

print(t1.timeit())

t1 = timeit.Timer('[x for x in data if x >= 0]', setup='from __main__ import data')

print(t1.timeit())

