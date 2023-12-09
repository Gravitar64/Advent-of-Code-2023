import time


def load(file):
  with open(file) as f:
    return [list(map(int, row.strip().split())) for row in f]


def get_next_number(sequenz, part1):
  if len(set(sequenz)) == 1: return sequenz[0]
  next_number = get_next_number([b - a for a, b in zip(sequenz, sequenz[1:])], part1)
  return sequenz[-1] + next_number if part1 else sequenz[0] - next_number


def solve(p, part1=True):
  return sum(get_next_number(sequenz, part1) for sequenz in p)


time_start = time.perf_counter()
puzzle = load("day09.txt")
print(f'Part 1: {solve(puzzle)}')
print(f'Part 2: {solve(puzzle,False)}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')