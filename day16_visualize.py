import time, pygame as pg


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]


def follow_beam(q, g):
  path, visited = [], set()
  while q:
    step, pos, dir = q.pop(0)
    if (pos, dir) in visited: continue
    visited.add((pos, dir))
    pos += dir
    if pos not in g: continue
    path.append((step, pos - dir, pos))
    match g[pos]:
      case '/': dir = -complex(dir.imag, dir.real)
      case '\\': dir = complex(dir.imag, dir.real)
      case '|':
        if dir.real != 0:
          dir = 0 + 1j
          q.append((step + 1, pos, -dir))
      case '-':
        if dir.imag != 0:
          dir = -1 + 0j
          q.append((step + 1, pos, -dir))
    q.append((step + 1, pos, dir))
  draw_beam(path,g)
  return len(set(pos for pos, dir in visited)) - 1


def paint_grid(grid, size):
  color = 'white'
  for pos, c in grid.items():
    if c == '.': continue
    x, y = pos.real * size, pos.imag * size
    hs = size / 2
    match c:
      case '-': pg.draw.line(fenster, color, (x, y + hs), (x + size, y + hs), 3)
      case '|': pg.draw.line(fenster, color, (x + hs, y), (x + hs, y + size), 3)
      case '\\': pg.draw.line(fenster, color, (x, y), (x + size, y + size), 3)
      case '/': pg.draw.line(fenster, color, (x + size, y), (x, y + size), 3)
  

def draw_beam(path,g):
  color = pg.Color(0)
  old_step = 0
  for step, p1, p2 in path:
    if step != old_step:
      old_step = step
      paint_grid(g,10)
      pg.display.flip()
      time.sleep(0.5)  # adjust the speed of the animaton
    f = p1.real * 10 + 5, p1.imag * 10 + 5
    t = p2.real * 10 + 5, p2.imag * 10 + 5
    color.hsva = (step % 360, 100, 100)
    pg.draw.line(fenster, color, f, t, 5)


def solve(p):
  grid = {complex(x, y): c for y, row in enumerate(p) for x, c in enumerate(row)}
  part1 = follow_beam([(0, -1 + 0j, 1 + 0j)], grid)
  return part1


puzzle = load("day16.txt")
pg.init()
size = 10
größe = breite, höhe = len(puzzle[0]) * size, len(puzzle) * size
fenster = pg.display.set_mode(größe)

time_start = time.perf_counter()
print(f'Part 1 & 2: {solve(puzzle)}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')