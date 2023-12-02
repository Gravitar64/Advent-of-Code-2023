import time
import re
import math


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]


def solve(p):
  target = dict(red=12, green=13, blue=14)
  boxes = [(re.findall('blue|red|green', row), list(map(int, re.findall('\d+', row)))) for row in p]
  part1 = sum(n[0] for c,n in boxes if all(target[color] >= amount for color,amount in zip(c,n[1:])))
  part2 = sum([math.prod([max(amount for c2, amount in zip(c,n[1:]) if c2 == c1) for c1 in target]) for c,n in boxes])
  return part1, part2


time_start = time.perf_counter()
puzzle = load('day02.txt')
part1, part2 = solve(puzzle)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
