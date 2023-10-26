import time
import re


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]
  

def solve(p):
  pass


time_start = time.perf_counter()
puzzle = load('day01.txt')
part1 = solve(puzzle)
print('Part 1: {part1}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')