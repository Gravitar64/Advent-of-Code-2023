import time, re, math, networkx


def load(file):
  with open(file) as f:
    return [re.findall('\w+', row) for row in f.readlines()]


def solve(p):
  g = networkx.Graph()
  g.add_edges_from((a,b) for a,*others in p for b in others)
  g.remove_edges_from(networkx.minimum_edge_cut(g))
  return math.prod(map(len, networkx.connected_components(g)))  


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day25.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')