import time, sys, collections


def load(file):
  with open(file) as f:
    return {complex(x, y): c for y, row in enumerate(f.readlines())
            for x, c in enumerate(row.strip()) if c != '#'}


def get_neighbors(p,pos,c,part1):
  if part1 and c != '.':
    return [pos + dirs[c]] 
  else:
    neighb = []
    for delta in dirs.values():
      if (pos2 := pos+delta) not in p: continue
      neighb.append(pos2)
    return neighb  


def dfs(G, node, target, dist, seen):
  if node == target: yield dist
  for pos in G[node]:
    if pos in seen: continue
    yield from dfs(G, pos, target, dist+1, seen | {pos})


def dfs2(G, node, target, dist, seen):
  if node == target: yield dist
  for pos, d in G[node]:
    if pos in seen: continue
    yield from dfs2(G, pos, target, dist + d, seen | {pos})
  
     
def solve(p):
  source = min(p, key=lambda x: (x.imag, x.real))
  target = max(p, key=lambda x: (x.imag, x.real))
  
  G1, G2 = dict(), dict()
  for pos,c in p.items():
    G1[pos] = get_neighbors(p,pos,c,True)
    G2[pos] = get_neighbors(p,pos,c,False)
  
  part1 = max(dfs(G1,source,target,0,{source}))

  junctions = [source] + [pos for pos,n in G2.items() if len(n) > 2] + [target]
  G = collections.defaultdict(list)
  for pos in junctions:
     for pos2 in G2[pos]:
       previous, cur = pos, pos2
       d = 1
       while cur not in junctions:
         previous, cur = cur, [pos3 for pos3 in G2[cur] if pos3 != previous][0]
         d += 1
       G[pos].append((cur, d))
  
  part2 = max(dfs2(G,source,target,0,{source}))
  
  return part1,part2


time_start = time.perf_counter()
sys.setrecursionlimit(10_000)
dirs = {'>': 1 + 0j, '<': -1 + 0j, 'v': 0 + 1j, '^': 0 - 1j}
print(f'Part 1: {solve(load("day23.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')