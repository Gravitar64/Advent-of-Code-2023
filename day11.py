import time, itertools


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]


def expand(galaxies, l, dir, exp):
  for e in reversed(l):
    if dir == 'r':
      galaxies = {(x, y + exp) if y > e else (x, y) for x, y in galaxies}
    else:
      galaxies = {(x + exp, y) if x > e else (x, y) for x, y in galaxies}
  return galaxies


def distances(galaxies):
  total = 0
  for a, b in itertools.combinations(galaxies, 2):
    total += sum(abs(d1 - d2) for d1, d2 in zip(a, b))
  return total


def solve(p, exp):
  galaxies = {(x, y) for y, row in enumerate(p) for x, c in enumerate(row) if c == '#'}
  rows, cols = [], []

  for row in range(len(p)):
    if [pos for pos in galaxies if pos[1] == row]: continue
    rows.append(row)

  for col in range(len(p[0])):
    if [pos for pos in galaxies if pos[0] == col]: continue
    cols.append(col)

  if rows: galaxies = expand(galaxies, rows, 'r', exp)
  if cols: galaxies = expand(galaxies, cols, 'c', exp)

  return distances(galaxies)


time_start = time.perf_counter()
puzzle = load("day11.txt")
print(f'Part 1: {solve(puzzle,1)}')
print(f'Part 1: {solve(puzzle,999_999)}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
