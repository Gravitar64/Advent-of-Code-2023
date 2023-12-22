import time
import pygame as pg
import random as rnd


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]
  

def follow_beam(q, g):
  path = []
  visited = set()
  while q:
    step, pos, dir = q.pop(0)
    if (pos,dir) in visited: continue
    visited.add((pos,dir))
    pos += dir
    if pos not in g: continue
    path.append((step, pos-dir,pos))
    match g.get(pos,None):
      case None: continue
      case '/':
        dir = -complex(dir.imag, dir.real)
      case '\\':
        dir = complex(dir.imag, dir.real)
      case '|':
        if dir.real != 0:
          dir = 0 + 1j
          q.append((step+1,pos,-dir))
      case '-':
        if dir.imag != 0:
          dir = -1 + 0j
          q.append((step+1,pos,-dir))
    q.append((step+1,pos,dir))          
  draw_beam(path)        
  return len(set(pos for pos,dir in visited)) - 1
        

def solve(p):
  grid = {complex(x,y) : c for y,row in enumerate(p) for x,c in enumerate(row)}
  paint_grid(grid,10)
  part1 = follow_beam([(0,-1 + 0j, 1 + 0j)], grid)
  
  #positions = ((pos - dir, dir) for dir in (1+0j, -1+0j, 0+1j, 0-1j) 
  #                              for pos in grid if pos - dir not in grid)
  #part2 = max(follow_beam([(pos,dir)], grid) for pos,dir in positions)
  return part1#, part2


def paint_grid(grid,size):
  color = 'green'
  for pos,c in grid.items():
    if c == '.': continue
    x,y = pos.real*size, pos.imag*size
    hs = size / 2
    match c:
      case '-' : pg.draw.line(fenster,color,(x,y+hs),(x+size,y+hs),3)
      case '|' : pg.draw.line(fenster,color,(x+hs,y),(x+hs,y+size),3)
      case '\\': pg.draw.line(fenster,color,(x,y),(x+size,y+size),3)
      case '/' : pg.draw.line(fenster,color,(x+size,y),(x,y+size),3)
  pg.display.flip()


def draw_beam(path):
  old_step = 0
  for step,p1,p2 in path:
    if step != old_step:
      old_step = step
      pg.display.flip()
      time.sleep(0.02)
    dir = p2-p1
    if dir.real != 0:
      ox,oy = 0,0
    else:
      ox,oy = 0,0  
    f = p1.real*10+ox, p1.imag*10+oy
    t = p2.real*10+ox, p2.imag*10+oy
    color = (rnd.randrange(256), rnd.randrange(256),rnd.randrange(256))
    pg.draw.line(fenster,color,f,t,5)
    

puzzle = load("day16.txt")
pg.init()

size = 10
größe = breite, höhe = len(puzzle[0])*size, len(puzzle)*size
fenster = pg.display.set_mode(größe)


clock = pg.time.Clock()

# Zeichenschleife mit FPS Bildern pro Sekunde



   
    

time_start = time.perf_counter()
print(f'Part 1 & 2: {solve(puzzle)}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')