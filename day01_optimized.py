import time
import re


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]
  

def get_number(row):
  numbers = re.findall('\d', row)
  return int(numbers[0] + numbers[-1])


def solve(p):
  replacements = [("one", "o1e"), ("two", "t2o"), ("three", "t3e"), ("four", "f4r"),
                  ("five", "f5e"), ("six", "s6x"), ("seven","s7n"), ("eight", "e8t"),
                  ("nine", "n9e")]
  
  part1 = part2 = 0
  for row in p:
    part1 += get_number(row)
    for a, b in replacements:
      row = row.replace(a, b)
    part2 += get_number(row)  
    
  return part1, part2


time_start = time.perf_counter()
puzzle = load('day01.txt')
part1, part2 = solve(puzzle)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')