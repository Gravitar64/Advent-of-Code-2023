import time, re, itertools, math


def load(file):
  with open(file) as f:
    return f.read().split('\n\n')


def solve(p):
  instructions, nodes = p
  nodes = [re.findall('\w+', row) for row in nodes.split('\n')]
  map_nodes = {node: dict(L=l, R=r) for node, l, r in nodes}
  starts, targets = [{node for node in map_nodes if node[-1] == lp} for lp in 'AZ']

  counts = []
  for start1 in starts:
    count, start2 = 0, start1
    for direction in itertools.cycle(instructions):
      count += 1
      start2 = map_nodes[start2][direction]
      if start2 in targets:
        counts.append(count)
        if start1 == 'AAA' and start2 == 'ZZZ': part1 = count
        break

  return part1, math.lcm(*counts)


time_start = time.perf_counter()
print(f'Solution: {solve(load("day08.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
