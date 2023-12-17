import time


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]
  

def follow_beam(q, g):
  visited = set()
  while q:
    pos, dir = q.pop()
    while not (pos,dir) in visited:
      visited.add((pos,dir))
      pos += dir
      match g.get(pos,None):
        case None: break
        case '/':
          dir = -complex(dir.imag, dir.real)
        case '\\':
          dir = complex(dir.imag, dir.real)
        case '|':
          dir = 0 + 1j
          q.append((pos,-dir))
        case '-':
          dir = -1 + 0j
          q.append((pos,-dir))
  return len(set(pos for pos, dir in visited)) - 1
        

def solve(p):
  grid = {complex(x,y) : c for y,row in enumerate(p) for x,c in enumerate(row)}
  part1 = follow_beam([(-1 + 0j, 1 + 0j)], grid)
  
  positions = ((pos - dir, dir) for dir in (1+0j, -1+0j, 0+1j, 0-1j) 
                                for pos in grid if pos - dir not in grid)
  part2 = max(follow_beam([(pos,dir)], grid) for pos,dir in positions)
  return part1, part2


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day16.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')