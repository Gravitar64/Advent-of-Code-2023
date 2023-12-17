import time, heapq


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]

def path(target,grid,least,most):
  q, visited = [(0, (0,0), (0,0))], set()

  while q:
    heat, pos, dir = heapq.heappop(q)
    if pos == target: return heat
    if (pos,dir) in visited: continue
    visited.add((pos,dir))

    (x,y), (dx,dy) = pos, dir
    for dir2 in {(0,1),(0,-1),(1,0),(-1,0)} - {(dx,dy), (-dx,-dy)}:
      h,(dx2,dy2) = heat, dir2
      
      for mul in range(1, most+1):
        pos2 = x + dx2 * mul, y + dy2 * mul
        if pos2 not in grid: break
        h += grid[pos2]
        if mul < least: continue
        heapq.heappush(q, (h, pos2, dir2))


def solve(p):
  grid = {(x,y):int(n) for y,row in enumerate(p) for x,n in enumerate(row)}
  part1 = path(max(grid),grid,1,3)
  part2 = path(max(grid),grid,4,10)

  return part1, part2


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day17.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')