import re

text = input().strip()
word = input().strip()

matches = re.findall(fr'{word}',text)
count = len(matches)

print(count)

# from re import findall, finditer
#
# result1 = findall(r'\w', 'beegeek')
# result2 = finditer(r'\w', 'beegeek')
#
# match1, *_ = result1
# match2, *_ = result2
#
# print(type(match1))
# print(type(match2))

#
# from itertools import repeat
#
# beegeek = ['bee', 'geek']
# repeater = repeat(beegeek)
#
# print(next(repeater))
#
# beegeek = beegeek + ['imposter']
#
# print(next(repeater))
# import itertools as it
# import time
#
# symbols = ['.', '-', "'", '"', "'", '-', '.', '_']
#
# for c in it.cycle(symbols):
#     print(c, end='')
#     time.sleep(0.05)