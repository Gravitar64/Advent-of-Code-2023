import time


def load(file):
  with open(file) as f:
    return f.read().split('\n\n')


def mirror(pattern):
  for reflection in range(1, len(pattern)):
    up, down = reflection - 1, reflection
    mirror = True

    while up >= 0 and down < len(pattern):
      if pattern[up] != pattern[down]:
        mirror = False
        break
      up, down = up - 1, down + 1

    if mirror: return reflection

  return 0


def smudge_mirror(pattern):
  for reflection in range(1, len(pattern)):
    up, down = reflection - 1, reflection
    diff = 0

    while up >= 0 and down < len(pattern):
      diff += sum(a != b for a, b in zip(pattern[up], pattern[down]))
      if diff > 1: break
      up, down = up - 1, down + 1

    if diff == 1: return reflection

  return 0


def solve(p):
  part1 = part2 = 0
  p = [s.split('\n') for s in p]
  for pattern in p:
    part1 += mirror(pattern) * 100 + mirror(list(zip(*pattern)))
    part2 += smudge_mirror(pattern) * 100 + smudge_mirror(list(zip(*pattern)))

  return part1, part2


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day13.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
