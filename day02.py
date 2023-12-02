import time
import re
from collections import defaultdict
import math


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]


def solve(p):
  part1 = part2 = 0
  target = dict(red=12, green=13, blue=14)
  
  for row in p:
    highest = defaultdict(int)
    colors = re.findall('blue|red|green', row)
    amounts = list(map(int, re.findall('\d+', row)))
    id = amounts.pop(0)
    for color, amount in zip(colors, amounts):
      highest[color] = max(highest[color], amount)
    if all(highest[color] <= target[color] for color in target): part1 += id
    part2 += math.prod(highest.values())

  return part1, part2


time_start = time.perf_counter()
puzzle = load('day02.txt')
part1, part2 = solve(puzzle)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
