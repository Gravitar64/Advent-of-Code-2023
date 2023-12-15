import time, collections


def load(file):
  with open(file) as f:
    return f.read().split(',')
  

def hash(s):
  result = 0
  for c in s:
    result = ((result + ord(c))*17) % 256
  return result  
  

def solve(p):
  part1 = sum(hash(s) for s in p)
  
  boxes = collections.defaultdict(dict)
  for s in p:
    if '=' in s:
      label, n = s.split('=')
      boxes[hash(label)][label]=int(n)
    else:
      label = s[:-1]
      boxes[hash(label)].pop(label,None)

  part2 = sum((bn+1) * ln * fl for bn, lenses in boxes.items()
                               for ln, fl in enumerate(lenses.values(), start = 1))
  return part1, part2


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day15.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')