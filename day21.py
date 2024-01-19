import time, numpy


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]
  

def solve(p):
  size = len(p)
  walls = {(x,y) for y, row in enumerate(p) for x,c in enumerate(row) if c == '#'}
  nodes = {(size//2, size//2)}
  neighb = lambda x,y: [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
  
  results = [1]
  for _ in range(1,65+131*2+1):
    nodes = {(x2,y2) for x,y in nodes for x2,y2 in neighb(x,y) if (x2%size,y2%size) not in walls}
    results.append(len(nodes))
  
  x = 26501365//131
  points = (results[65], results[65+131], results[65+131*2])
  a,b,c = map(round,numpy.poly1d(numpy.polyfit([0,1,2], points, 2)))
    
  return results[64], a*x**2 + b*x + c


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day21.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')