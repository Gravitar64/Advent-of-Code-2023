from ursina import *
import time, re, collections


def load(file):
  with open(file) as f:
    return [list(map(int,re.findall('\d+',row))) for row in f.readlines()]


def drop(bricks, skip=None):
  peaks, falls = collections.defaultdict(int), 0
  
  for i, (x1, y1, z1, x2, y2, z2) in enumerate(bricks):
    if i == skip: continue
    area = [(a, b) for a in range(x1, x2 + 1) for b in range(y1, y2 + 1)]
    peak = max(peaks[a] for a in area) + 1
    for a in area: peaks[a] = peak + z2 - z1
    if peak == z1: continue
    bricks[i] = [x1, y1, peak, x2, y2, peak + z2 - z1]
    falls += 1
  
  return not falls, falls


def solve(p):
  bricks = sorted(p,key=lambda brick:brick[2])
  for (x1,y1,z1,x2,y2,z2) in bricks:
    sx,sy,sz = x2-x1+1, y2-y1+1, z2-z1+1
    c = color.random_color()
    e = Entity(model='cube',position=Vec3(x1,y1,z1),scale_x=sx, scale_y=sy, scale_z=sz, color=c)
    
  app.run()

  drop(bricks)
  return [*map(sum, zip(*[drop(bricks.copy(), skip=i) for i in range(len(bricks))]))]


app = Ursina()
window.borderless = False
window.size = (800,800)
window.position = (2000, 200)
EditorCamera()

time_start = time.perf_counter()
print(f'Part 1 & 2: {solve(load("day22.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')