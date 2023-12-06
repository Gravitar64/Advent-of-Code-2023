import time, re, math


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]


def solve(p, part1=True):
  part = 1
  times, records = [map(int, re.findall('\d+', row if part1 else row.replace(' ', ''))) for row in p]
  for time, record in zip(times, records):
    high = math.floor((time + (time**2 - 4 * (record+1))**0.5)/2)
    low = math.ceil((time - (time**2 - 4 * (record+1))**0.5)/2)
    part *= high - low + 1
  return part


time_start = time.perf_counter()
puzzle = load("day06.txt")
print(f'Part 1: {solve(puzzle)}')
print(f'Part 2: {solve(puzzle, False)}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
