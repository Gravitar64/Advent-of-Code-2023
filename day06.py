import time
import re


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]


def solve(p, part1=True):
  part = 1
  times, distances = [map(int, re.findall('\d+', row if part1 else row.replace(' ', ''))) for row in p]
  for time, record in zip(times, distances):
    solutions = 0
    for button in range(1, time):
      if (time - button) * button > record: solutions += 1
    part *= solutions
  return part


time_start = time.perf_counter()
puzzle = load("day06.txt")
print(f'Part 1: {solve(puzzle)}')
print(f'Part 2: {solve(puzzle, False)}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
