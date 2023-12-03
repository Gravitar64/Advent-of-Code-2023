import time, re, math


def load(file):
  with open(file) as f:
    return f.read()


def adjacents(matches, rl):
  return {match.span()[0] + delta for match in matches for delta in (-rl - 1, -rl, -rl + 1, -1, 1, rl - 1, rl, rl + 1)}


def numbers_positions(matches):
  return [(int(match.group()), set(range(match.span()[0], match.span()[1]))) for match in matches]


def solve(p):
  row_lenght = p.index('\n') + 1
  numbers = numbers_positions(re.finditer('\d+', p))
  symbols = adjacents(re.finditer('[^0-9.\n]', p), row_lenght)
  gears = [adjacents([match], row_lenght) for match in re.finditer('\*', p)]

  part1 = sum(n for n, p in numbers if p & symbols)
  part2 = sum(math.prod(gn) 
              if len(gn := [n for n, p in numbers if p & gear]) == 2 else 0 
              for gear in gears)
  
  return part1, part2


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day03.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
