import time, re


def load(file):
  with open(file) as f:
    return [list(map(int,re.findall('\d+',row))) for row in f.readlines()]


def settle(segments):
  bricks = set((z,x,y) for segment in segments for z,x,y in segment)
  for i,segment in enumerate(segments):
    falling = True
    while falling:
      for (z,x,y) in segment:
        if z < 2: 
          falling = False
          break
        new_brick = z-1,x,y
        if new_brick in (bricks - {(z,x,y) for z,x,y in segment}): 
          falling = False
          break
      else:
        segment_new = [(z-1,x,y) for z,x,y in segment]
        segments[i] = segment_new
        bricks = bricks - {(z,x,y) for z,x,y in segment} | {(z,x,y) for z,x,y in segments[i]}
        segment = segment_new
  return segments


def can_disintegrated(segments):
  counter = 0
  segs = []
  for segment in segments:
    maxZ = max(z for z,_,_ in segment)
    bricks = set((z,x,y) for s in segments for z,x,y in s if s != segment)
    above = [s for s in segments if any(z == maxZ+1 for z,x,y in s)]
    if not above:
      counter += 1
      segs.append(segment)
      continue
    can_fall = False
    for segment2 in above:
      if can_fall: break
      for (z,x,y) in segment2:
        new_brick = z-1,x,y
        if new_brick in (bricks - {(z,x,y) for z,x,y in segment2}): break
      else:
        can_fall = True  
    if not can_fall:
      segs.append(segment)
      counter += 1
  return counter, segs  

def solve(p):
  segments = []
  for x1,y1,z1,x2,y2,z2 in p:
    segment = []
    for z in range(z1,z2+1):
      for x in range(x1,x2+1):
        for y in range(y1,y2+1):
          segment.append((z,x,y))
    segments.append(segment)      
  segments = settle(sorted(segments))
  return can_disintegrated(segments)
    





  


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day22.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')