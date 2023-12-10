import time


def load(file):
  with open(file) as f:
    return [list(map(int, row.strip().split())) for row in f]


def get_next_number(sequence):
  if len(set(sequence)) == 1: return sequence[0]
  next_number = get_next_number([b - a for a, b in zip(sequence, sequence[1:])])
  return sequence[-1] + next_number


def solve(p):
  part1 = sum(get_next_number(sequence) for sequence in p)
  part2 = sum(get_next_number(sequence[::-1]) for sequence in p)
  return part1, part2


time_start = time.perf_counter()
print(f'Part 1 & 2:{solve(load("day09.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')