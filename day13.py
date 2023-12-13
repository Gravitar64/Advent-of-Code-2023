import time


def load(file):
  with open(file) as f:
    return f.read().split('\n\n')


def mirror(pattern):
  for start in range(1, len(pattern)):
    low, high = start - 1, start
    is_mirror = True

    while low >= 0 and high < len(pattern):
      if pattern[low] != pattern[high]:
        is_mirror = False
        break
      low, high = low - 1, high + 1

    if is_mirror: return start

  return 0


def mirror_smudge(pattern):
  for start in range(1, len(pattern)):
    low, high = start - 1, start
    diff = 0

    while low >= 0 and high < len(pattern):
      diff += sum(a != b for a, b in zip(pattern[low], pattern[high]))
      if diff > 1: break
      low, high = low - 1, high + 1

    if diff == 1: return start

  return 0


def solve(p):
  part1 = part2 = 0
  patterns = [pattern.split('\n') for pattern in p]

  for pattern in patterns:
    part1 += mirror(pattern) * 100 + mirror(list(zip(*pattern)))
    part2 += mirror_smudge(pattern) * 100 + mirror_smudge(list(zip(*pattern)))

  return part1, part2


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day13.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
