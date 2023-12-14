import time


def load(file):
  with open(file) as f:
    return [s.split('\n') for s in f.read().split('\n\n')]


def mirror(pattern, smudges):
  for axis in range(1, len(pattern)):
    above, below = reversed(pattern[:axis]), pattern[axis:]
    if sum(c1 != c2 for a, b in zip(above, below) for c1, c2 in zip(a, b)) == smudges: return axis
  return 0


def solve(p):
  part1 = part2 = 0
  for pattern in p:
    part1 += mirror(pattern, 0) * 100 + mirror(list(zip(*pattern)), 0)
    part2 += mirror(pattern, 1) * 100 + mirror(list(zip(*pattern)), 1)
  return part1, part2


time_start = time.perf_counter()
print(f'Part 1 & 2: {solve(load("day13.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
