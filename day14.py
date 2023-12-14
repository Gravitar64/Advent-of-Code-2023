import time


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]


def points(p):
  return sum(row.count('O') * (len(p) - i) for i, row in enumerate(p))


def roll(p):
  p = [''.join(col) for col in zip(*p)]
  p = ['#'.join(''.join(sorted(sub, reverse=True)) for sub in row.split('#')) for row in p]
  return [''.join(col) for col in zip(*p)]


def cycle(p):
  for _ in range(4):
    p = [''.join(col) for col in zip(*p)]
    p = ['#'.join(''.join(sorted(sub, reverse=True)) for sub in row.split('#')) for row in p]
    p = [row[::-1] for row in p]
  return p


def solve(p):
  part1 = points(roll(p))

  pattern = [p]
  while True:
    p = cycle(p)
    if p in pattern: break
    pattern.append(p)

  offset = pattern.index(p)
  cycle_length = len(pattern) - offset
  part2 = points(pattern[(1_000_000_000 - offset) % cycle_length + offset])

  return part1, part2


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day14.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
