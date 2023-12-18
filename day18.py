import time
import shapely


def load(file):
  with open(file) as f:
    return [row.strip().split() for row in f]


def solve(p, part1):
  dirs = dict(R=(1, 0), D=(0, 1), L=(-1, 0), U=(0, -1))
  dirs2 = [dir for dir in dirs.values()]
  x = y = 0
  corners = [(x, y)]
  for dir, l, color in p:
    if part1:
      dx, dy = dirs[dir]
    else:
      l = int(color[2:-2], 16)
      dx, dy = dirs2[int(color[-2])]
    x, y = x + dx * int(l), y + dy * int(l)
    corners.append((x, y))
  pgon = shapely.Polygon(corners)
  return int(pgon.area + pgon.length / 2 + 1)


time_start = time.perf_counter()
puzzle = load("day18.txt")
print(f'Part 1: {solve(puzzle,True)}')
print(f'Part 2: {solve(puzzle,False)}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
