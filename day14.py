import time, re


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]
  

def rolling(col):
  for pos, rock in enumerate(col):
    if rock != 'O': continue
    rolling_north = pos
    while True:
      rolling_north -= 1
      if rolling_north < 0: break
      if col[rolling_north] in '#O': break
    if rolling_north+1 != pos:
      col[rolling_north+1] = 'O'
      col[pos] = '.'  
  return col  
  

def solve(p):
  part1 = 0
  p = list(zip(*p))
  for i,col in enumerate(p):
    p[i] = rolling(list(col))
  for i,col in enumerate(list(zip(*p))):
    for rock in col:
      if rock != 'O': continue
      part1 += len(p)-i
  return part1    
    


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day14.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')