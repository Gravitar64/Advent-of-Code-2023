import time


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]


def total_load(p):
  return sum(row.count('O') * (len(p) - i) for i, row in enumerate(p))


def roll(p):
  p = [''.join(a) for a in zip(*p)]
  p = ['#'.join(''.join(sorted(sub, reverse=True)) for sub in row.split('#')) for row in p]
  return [''.join(a) for a in zip(*p)]


def cycle(p):
  for _ in range(4):
    p = [''.join(a) for a in zip(*p)]
    p = ['#'.join(''.join(sorted(sub, reverse=True)) for sub in row.split('#')) for row in p]
    p = [row[::-1] for row in p]
  return p


def solve(p):
  part1 = total_load(roll(p))

  patterns = [p]
  while True:
    p = cycle(p)
    if p in patterns: break
    patterns.append(p)

  hit = len(patterns)
  offset = patterns.index(p)
  cycle_length = hit - offset
  print(hit, offset, cycle_length)
  part2 = total_load(patterns[(1_000_000_000 - offset) % cycle_length + offset])

  return part1, part2


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day14.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
