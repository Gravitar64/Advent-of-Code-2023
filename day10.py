import time


def load(file):
  with open(file) as f:
    return [row.strip() for row in f]


def bfs(grid, directions, connections):
  start = [pos for pos, c in grid.items() if c == 'S'][0]
  queue, seen = [(0, start)], set()
  while queue:
    count, (x, y) = queue.pop(0)
    seen.add((x, y))
    for dx, dy in directions[grid[x, y]]:
      x2, y2 = x + dx, y + dy
      if (x2, y2) not in grid or (x2, y2) in seen: continue
      if grid[x2, y2] not in connections[dx, dy]:  continue
      queue.append((count + 1, (x2, y2)))
  return count, seen


def is_inside(grid, x, y, size):
  counter = 0
  for _ in range(size):
    x -= 1
    if x < 0: break
    counter += grid.get((x, y), 'X') in '|JL'
  return counter % 2


def solve(p):
  N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)
  directions = {'S': [N, S, W, E], '|': [N, S], '-': [E, W],
                'L': [N, E], 'J': [N, W], '7': [S, W], 'F': [S, E]}
  connections = {N: {'|', '7', 'F'}, S: {'|', 'L', 'J'},
                E: {'-', 'J', '7'}, W: {'-', 'L', 'F'}}

  grid = {(x, y): c for y, row in enumerate(p)
          for x, c in enumerate(row) if c != '.'}
  part1, seen = bfs(grid, directions, connections)

  part2 = 0
  loop = {(x, y): c for (x, y), c in grid.items() if (x, y) in seen}
  min_x, max_x = min(seen)[0], max(seen)[0]
  min_y, max_y = min(s[1] for s in seen), max(s[1] for s in seen)
  
  for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
      if (x, y) in loop: continue
      part2 += is_inside(loop, x, y, max_x)

  return part1, part2


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day10.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')