import time


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]
  

def solve(p):
  gardens = {(x,y) for y,row in enumerate(p) for x,c in enumerate(row) if c != '#'}
  size = len(p) 
  S = (size//2, size//2) #allways quadratic, allways in the centre
  
  k,r =divmod(26501365,size)
  visited, new, cache = {S}, {S}, {0:1}

  for n in range(1,2*size+r+1): #simulate till reached end off 2nd tile to the right
    visited, new = new, {(x2,y2) for x,y in new for x2,y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1))
                         if (x2,y2) not in visited and (x2%size, y2%size) in gardens}
    cache[n] = len(new) + (cache[n-2] if n > 1 else 0)
  
  d1 = cache[2*size+r] - cache[r+size]
  d2 = cache[2*size+r] + cache[r] - 2*cache[r+size]
  part1 = cache[64]
  part2 = cache[2*size+r]+(k-2)*(2*d1+(k-1)*d2)//2

  return part1, part2


time_start = time.perf_counter()
print(f'Part 1 & 2: {solve(load("day21.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')