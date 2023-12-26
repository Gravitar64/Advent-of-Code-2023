import time, sys, collections


def load(file):
  with open(file) as f:
    return {complex(x, y): c for y, row in enumerate(f.readlines())
            for x, c in enumerate(row.strip()) if c != '#'}


def neigb(p, pos, part1):
  if part1 and p[pos] != '.':
    return [pos + dirs[p[pos]]]
  else:
    return [pos + delta for delta in dirs.values() if pos + delta in p]


def dfs(p, node, target, dist, seen):
  if node == target: yield dist
  for pos in neigb(p, node, True):
    if pos in seen: continue
    yield from dfs(p, pos, target, dist + 1, seen | {pos})


def dfs2(g, node, target, dist, seen):
  if node == target: yield dist
  for pos, d in g[node]:
    if pos in seen: continue
    yield from dfs2(g, pos, target, dist + d, seen | {pos})


def compress_graph(p, source, target):
  g = collections.defaultdict(list)
  junctions = {source} | {pos for pos in p if len(neigb(p, pos, False)) > 2} | {target}
  for pos in junctions:
    for pos2 in neigb(p, pos, False):
      prev, cur = pos, pos2
      d = 1
      while cur not in junctions:
        prev, cur = cur, [pos3 for pos3 in neigb(p, cur, False) if pos3 != prev][0]
        d += 1
      g[pos].append((cur, d))
  return g


def solve(p):
  source = min(p, key=lambda x: (x.imag, x.real))
  target = max(p, key=lambda x: (x.imag, x.real))
  part1 = max(dfs(p, source, target, 0, {source}))

  g = compress_graph(p, source, target)
  part2 = max(dfs2(g, source, target, 0, {source}))

  return part1, part2


time_start = time.perf_counter()
sys.setrecursionlimit(10_000)
dirs = {'>': 1 + 0j, '<': -1 + 0j, 'v': 0 + 1j, '^': 0 - 1j}
print(f'Part 1: {solve(load("day23.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')