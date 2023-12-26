import time, re, collections


def load(file):
  with open(file) as f:
    return [re.findall('\w+', row) for row in f.readlines()]


def solve(p):
  g = collections.defaultdict(set)
  for u, *vs in p:
    for v in vs: 
      g[u].add(v)
      g[v].add(u)
  
  s=set(g)
  count = lambda x: len(g[x]-s)

  while sum(map(count,s)) != 3:
    s.remove(max(s, key=count))

  return len(s) * len(set(g) - s)      



time_start = time.perf_counter()
print(f'Part 1: {solve(load("day25.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
