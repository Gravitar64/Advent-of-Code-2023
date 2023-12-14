import time


def load(file):
  with open(file) as f:
    return [row.strip() for row in f.readlines()]


def roll(p):
  p = [''.join(a) for a in zip(*p)]
  p = ['#'.join(''.join(sorted(s, reverse=True)) for s in row.split('#')) for row in p]
  return [''.join(a) for a in zip(*p)]


def cycle(p):
  for _ in range(4):
    p = [''.join(a) for a in zip(*p)]
    p = ['#'.join(''.join(sorted(s, reverse=True)) for s in row.split('#')) for row in p]
    p = [row[::-1] for row in p]
  return p


def total_load(p):
  return sum(col.count('O') * (len(p) - i) for i, col in enumerate(p))


def solve(p):
  part1 = total_load(roll(p))

  patterns, seen, counter = [p], {tuple(p)}, 0
  while True:
    counter += 1
    p = tuple(cycle(p))
    if p in seen: break
    patterns.append(p)
    seen.add(p)

  offset = patterns.index(p)
  cycle_length = counter - offset
  part2 = total_load(patterns[(1_000_000_000 - offset) % cycle_length + offset])

  return part1, part2


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day14.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')