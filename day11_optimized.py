import time
from itertools import combinations


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]


def expand(galaxies, empties, exp):
  for n, row in reversed(empties):
    if row:
      galaxies = [(x, y + exp) if y > n else (x, y) for x, y in galaxies]
    else:
      galaxies = [(x + exp, y) if x > n else (x, y) for x, y in galaxies]
  return galaxies


def distances(galaxies):
  return sum(abs(d1 - d2) for a, b in combinations(galaxies, 2) for d1, d2 in zip(a, b))


def solve(p):
  galaxies = [(x, y) for y, row in enumerate(p) for x, c in enumerate(row) if c == '#']
  cols, rows = [{pos[d] for pos in galaxies} for d in (0,1)]

  empties = [(n,True) for n in (set(range(len(p))) - rows)]
  empties += [(n,False) for n in (set(range(len(p[0]))) - cols)]
  empties.sort()
  
  g1 = expand(galaxies, empties, 1)
  g2 = expand(galaxies, empties, 999_999)
  
  return distances(g1), distances(g2)


time_start = time.perf_counter()
print(f'Part 1 & 2: {solve(load("day11.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')