import time


def load(file):
  with open(file) as f:
    return [row.strip().split() for row in f]
  

def flood_fill(trenches):
  x,y = min(trenches)
  dx,dy = 1,1
  while True:
    x,y = x+dx, y+dy
    if (x,y) in trenches: continue
    break

  q = [(x,y)]
  while q:
    x,y = q.pop(0)
    trenches.add((x,y))
    for x2,y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
      if (x2,y2) in trenches: continue
      q.append((x2,y2))
      trenches.add((x2,y2))
  return trenches
    
    
def solve(p,part1):
  dirs = dict(R=(1,0), D=(0,1), L=(-1,0), U=(0,-1))
  dirs2 = [dir for dir in dirs.values()]
  x,y = 0,0
  trenches = {(x,y)}
  for dir, l, color in p:
    if part1:
      dx,dy = dirs[dir]
      for _ in range(int(l)):
        x,y = x+dx, y+dy
        trenches.add((x,y))
    else:
      l = int(color[2:-2],16)
      dx,dy = dirs2[int(color[-2])]
      for _ in range(int(l)):
        x,y = x+dx, y+dy
        trenches.add((x,y))  

  trenches = flood_fill(trenches)
  return len(trenches)
    

time_start = time.perf_counter()
puzzle = load("day18.txt")
print(f'Part 1: {solve(puzzle, True)}')
print(f'Part 2: {solve(puzzle, False)}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')