import time, functools


def load(file):
  with open(file) as f:
    return [row.strip().split() for row in f]


@functools.cache
def count(spr, gr):
  spr = spr.lstrip('.')
  if not spr:
    return not gr
  if not gr:
    return '#' not in spr

  if spr[0] == '#':
    if len(spr) < gr[0] or '.' in spr[:gr[0]] or spr[gr[0]] == '#': return 0
    return count(spr[gr[0] + 1:], gr[1:])

  return count('#' + spr[1:], gr) + count(spr[1:], gr)


def solve(p):
  part1 = part2 = 0

  for springs, groups in p:
    groups = tuple(int(n) for n in groups.split(','))
    part1 += count(springs + '.', groups)
    part2 += count((springs + '?') * 4 + springs + '.', groups * 5)

  return part1, part2


time_start = time.perf_counter()
print(f'Part 1 & 2: {solve(load("day12.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
