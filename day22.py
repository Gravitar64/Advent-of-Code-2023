import time, re 
from skspatial.objects import LineSegment, Vector
import itertools


def load(file):
  with open(file) as f:
    return [list(map(int,re.findall('\d+',row))) for row in f.readlines()]
  

def solve(p):
  lines = [LineSegment(coords[:3], coords[3:]) for coords in p]
  gravity = Vector([0,0,-1])
  for a,b in itertools.combinations(lines,2):
    a = LineSegment(a.point_a+gravity, a.point_b+gravity)
    try:
      a.intersect_line_segment(b)
      print(a,b)
    except:
      print('No Intersection')  

  for a,b in itertools.combinations(lines,2):
    try:
      print(a.intersect_line_segment(b))
      print(a,b)
    except:
      pass


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day22.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')