import time


def load(file):
  with open(file) as f:
    return [row.strip().split() for row in f]
  

def f(steps, pos=0, ans=1):
  for (x,y), n in steps:
    pos += x*n
    ans += y*n * pos + n/2
  return int(ans)


def solve(p):
  dirs = {'R':(1, 0), 'D':(0, 1), 'L': (-1, 0), 'U':(0, -1),
          '0':(1, 0), '1':(0, 1), '2': (-1, 0), '3':(0, -1)}
  
  part1 = f((dirs[d],     int(s))           for d,s,_ in p)
  part2 = f((dirs[c[-2]], int(c[2:-2],16))  for _,_,c in p)

  return part1, part2


time_start = time.perf_counter()
puzzle = load("day18.txt")
print(f'Part 1 & 2: {solve(load("day18.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
