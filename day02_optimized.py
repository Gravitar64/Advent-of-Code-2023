import time
import re
import math


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]


def solve(p):
  target = dict(red=12, green=13, blue=14)
  bags = [[box.split() for box in re.findall('\d+ \w+', row)] for row in p]
  part1 = sum(i for i,bag in enumerate(bags,start=1) if all(target[c] >= int(n) for n,c in bag))
  part2 = sum([math.prod([max(int(n) for n,c2 in bag if c2 == c1) for c1 in target]) for bag in bags])
  return part1, part2


time_start = time.perf_counter()
print(f'Solution: {solve(load("day02.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')