import time, itertools, re


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]


def adjacents(x, y):
  adj = set()
  for dx, dy in itertools.product(range(-1, 2), repeat=2):
    adj.add((x + dx, y + dy))
  return adj


def is_adjacent(positions, symbols):
  return set(positions) & symbols


def solve(p):
  part1 = part2 = 0
  
  numbers, symbols, gears = [], set(), set()
  for y, row in enumerate(p):
    number, positions = '', set()
    for x, c in enumerate(row):
      if c.isdigit():
        number += c
        positions.add((x, y))
      else:
        if c != '.':  
          symbols.update(adjacents(x, y))
          if c == '*': gears.add(frozenset(adjacents(x,y)))
      if number and (not c.isdigit() or x == len(row)-1):
        numbers.append((int(number),positions))
        number, positions = '', set()
   
  for number, positions in numbers:
    if not is_adjacent(positions, symbols): continue
    part1 += number

  for pos1 in gears:
    gear_numbers = []
    for number, pos2 in numbers:
      if  set(pos2) & pos1: gear_numbers.append(number)
    if len(gear_numbers) == 2:
      part2 += gear_numbers[0] * gear_numbers[1]       
    
  return part1,part2


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day03.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
