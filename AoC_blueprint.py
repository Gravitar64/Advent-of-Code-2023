import time, re


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]
  

def solve(p):
  return p


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day01.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')