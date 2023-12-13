import time


def load(file):
  with open(file) as f:
    return f.read().split('\n\n')


def mirror(pattern, vertical):
  pattern = list(zip(*pattern)) if vertical else pattern
  for start in range(1,len(pattern)):
    for dy in range(start):
      if start - dy -1 >= 0 and start + dy < len(pattern):
        if pattern[start - dy - 1] == pattern[start + dy]: continue
        break
    else:  
      return start
  return 0


def mirror_smudge(pattern, vertical):
  pattern = list(zip(*pattern)) if vertical else pattern
  for start in range(1,len(pattern)):
    diff = 0
    for dy in range(start):
      if start - dy -1 >= 0 and start + dy < len(pattern):
        diff += sum(a != b for a,b in zip(pattern[start-dy-1], pattern[start +dy]))
        if diff > 1: break
    if diff == 1: return start  
  return 0


def solve(p):
  part1 = part2 = 0
  patterns = [pattern.split('\n') for pattern in p]
  
  for pattern in patterns:
    part1 += mirror(pattern,False) * 100 + mirror(pattern,True)
    part2 += mirror_smudge(pattern,False) * 100 + mirror_smudge(pattern,True)
  
  return part1, part2


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day13.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
