import time, numpy


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]


def solve(p):
  size = len(p)
  walls = {(x, y) for y, row in enumerate(p) for x, c in enumerate(row) if c == '#'}
  nodes, results = {(size//2, size//2)}, [1]
  neig = lambda x,y: [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
  
  for _ in range(1, 65+131*2+1):
    nodes = {(x2,y2) for x,y in nodes for x2,y2 in neig(x,y) if (x2%size,y2%size) not in walls}
    results.append(len(nodes))

  part1 = results[64]
  
  points = [results[n] for n in (65, 65 + 131, 65 + 2 * 131)]
  x = 26501365 // size
  a, b, c = map(round, numpy.poly1d(numpy.polyfit([0, 1, 2], points, 2)))
  part2 = a * x**2 + b * x + c
  
  return part1, part2


time_start = time.perf_counter()
print(f'Part 1 & 2: {solve(load("day21.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
