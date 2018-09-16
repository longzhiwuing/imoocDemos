from random import randint, sample
from functools import reduce

# print(sample('abcdefg', randint(3,6)))

# 统计每一个s都有相同key

s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

print(s1)
print(s2)
print(s3)

# print(s1.keys())

res = map(dict.keys, [s1, s2, s3])

result = reduce(lambda a, b: a & b, res)

print(result)
