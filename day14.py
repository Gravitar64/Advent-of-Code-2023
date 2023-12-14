import time


def load(file):
  with open(file) as f:
    return [[c for c in row.strip()] for row in f.readlines()]
  

def rolling(pattern):
  for _ in range(4):
    pattern = list(list(a) for a in zip(*pattern))
    for i,col in enumerate(pattern):
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
      pattern[i] = col
    pattern = [row[::-1] for row in pattern]
  return pattern      


        
def solve(p):
  hash = tuple(''.join(row) for row in p)
  patterns, seen = [hash], set(hash)
  counter = 0
  while True:
    counter += 1
    p = rolling(p)
    hash = tuple(''.join(row) for row in p)
    if hash in seen: break
    patterns.append(hash)
    seen.add(hash)
  offset = patterns.index(hash)
  p = patterns[(1_000_000_000 - offset) % (counter - offset) + offset]
  return sum(col.count('O')*(len(p)-i) for i,col in enumerate(p))
  


    


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day14.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')