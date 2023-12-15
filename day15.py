import time, collections


def load(file):
  with open(file) as f:
    return f.read().split(',')
  

def hash(s):
  h = 0
  for c in s:
    h = ((h+ord(c))*17) % 256
  return h  


def solve(p):
  part1 = sum(hash(s) for s in p)

  boxes = collections.defaultdict(dict)
  for s in p:
    if '=' in s:
      lense, fl = s.split('=')
      boxes[hash(lense)][lense] = int(fl)
    else:
      lense = s[:-1]
      boxes[hash(lense)].pop(lense,None)

  part2 = sum((bn+1) * ln * fl 
              for bn, lenses in boxes.items()
              for ln, fl in enumerate(lenses.values(),start=1))  
      
  return part1, part2


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day15.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')