import time, re, collections


def load(file):
  with open(file) as f:
    return [list(map(int,re.findall('\d+',row))) for row in f]
  

def drop(p,skip):
  hight_map = collections.defaultdict(int)
  fallen = 0
  for i, (x1,y1,z1,x2,y2,z2) in enumerate(p):
    if i == skip: continue
    poss = [(x,y) for x in range(x1,x2+1) for y in range(y1,y2+1)]
    lowest = max(hight_map[pos] for pos in poss) + 1
    for pos in poss:
      hight_map[pos] = lowest + z2 - z1
    if lowest == z1: continue
    fallen += 1
    if skip == None: p[i] = [x1,y1,lowest,x2,y2,lowest +z2 - z1]
  return not fallen, fallen   

  
def solve(p):
  part1 = part2 = 0
  p = sorted(p,key=lambda x:x[2])
  drop(p, None)
  for i in range(len(p)):
    disintegrated, fallen = drop(p,i)
    part1 += disintegrated
    part2 += fallen

  return part1, part2


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day22.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')