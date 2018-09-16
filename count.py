from random import randint
from collections import Counter
import re

#统计词频
txt = open('d:\\test.txt', encoding='utf-8').read()
list = re.split('\W+',txt)

c3 = Counter(list)

print(c3.most_common(3))


# data = [randint(0, 20) for _ in range(30)]
#
# dic2 = Counter(data)
#
# print(dic2)
#
# print(dic2.most_common(3))


#
# # print(data)
#
# dic = dict.fromkeys(data, 0)
#
# # print(dic)
#
# for x in data:
#     dic[x] += 1
#
# print(dic)
