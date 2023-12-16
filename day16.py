import time


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]
  

def follow_beam(x,y,dx,dy,p):
  w,h = len(p[0]), len(p)
  seen, queue = set(), [(x,y,dx,dy)]
  while queue:
    x,y,dx,dy = queue.pop(0)
    x,y = x+dx, y+dy
    if x < 0 or x >= w or y < 0 or y >= h : continue
    ch = p[y][x]
    if ch == '.' or ch == '-' and dx != 0 or ch == '|' and dy != 0: 
      if (x,y,dx,dy) not in seen:
        seen.add((x,y,dx,dy))
        queue.append((x,y,dx,dy))
    elif p[y][x] == '/':
      dy,dx = -dx, -dy
      if (x,y,dx,dy) not in seen:
        seen.add((x,y,dx,dy))
        queue.append((x,y,dx,dy))
    elif p[y][x] == '\\':
      dy,dx = dx, dy
      if (x,y,dx,dy) not in seen:
        seen.add((x,y,dx,dy))
        queue.append((x,y,dx,dy))
    else:
      for dy,dx in [(1,0), (-1,0)] if ch == '|' else [(0,1), (0,-1)]:
        if (x,y,dx,dy) not in seen:
          seen.add((x,y,dx,dy))
          queue.append((x,y,dx,dy))    
    
  return len({(x,y) for x,y,_,_ in seen})


def solve(p):
  part1 = follow_beam(-1,0,1,0,p)

  part2 = 0
  for row in range(len(p)):
    part2 = max(part2, follow_beam(-1,row,1,0,p))
    part2 = max(part2, follow_beam(len(p[0]),row,-1,0,p))
  for col in range(len(p[0])):
    part2 = max(part2, follow_beam(col,-1,0,1,p))
    part2 = max(part2, follow_beam(col,len(p),0,-1,p))

  return part1, part2  


   



time_start = time.perf_counter()
print(f'Part 1: {solve(load("day16.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')