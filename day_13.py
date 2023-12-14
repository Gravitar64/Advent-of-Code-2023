import time


def load(file):
  with open(file) as f:
    return [s.split('\n') for s in f.read().split('\n\n')]


def mirror(pattern, part1):
  for axis in range(1, len(pattern)):
    above, below = reversed(pattern[:axis]), pattern[axis:]
    if part1:
      if all(a == b for a, b in zip(above, below)): return axis
    else:
      if sum(c1 != c2 for a, b in zip(above, below) for c1, c2 in zip(a, b)) == 1: return axis
  return 0


def solve(p,part1):
  result = 0
  for pattern in p:
    result += mirror(pattern, part1) * 100 + mirror(list(zip(*pattern)), part1)
  return result


time_start = time.perf_counter()
puzzle = load("day13.txt")
print(f'Part 1: {solve(puzzle, True)}')
print(f'Part 2: {solve(puzzle, False)}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
