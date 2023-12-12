import time, functools


def load(file):
  with open(file) as f:
    return [row.strip().split() for row in f]
  

@functools.cache
def count(springs, groups):
  springs = springs.lstrip('.')
  if not springs: return not groups
  if not groups: return '#' not in springs

  if springs[0] == '#':
    if len(springs) < groups[0] or '.' in springs[:groups[0]]:
      return 0
    elif len(springs) == groups[0]:
      return len(groups) == 1
    elif springs[groups[0]] == '#':
      return 0
    else:
      return count(springs[groups[0]+1:], groups[1:])

  return count('#' + springs[1:], groups) + count(springs[1:], groups)  
  

def solve(p):
  part1 = part2 = 0
  
  for springs, groups in p:
    groups = tuple(int(n) for n in groups.split(','))
    part1 += count(springs, groups)
    part2 += count((springs+'?')*4 + springs, groups*5)

  return part1, part2  


time_start = time.perf_counter()
print(f'Part 1 & 2: {solve(load("day12.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')