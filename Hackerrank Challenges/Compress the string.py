#https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby

print(*[(len(list(c)), int(x)) for x, c in groupby(input())])