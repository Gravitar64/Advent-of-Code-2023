import time, re, itertools


def load(file):
  with open(file) as f:
    return [[int(x) for x in re.findall('-?\d+', row)] for row in f.readlines()]


def dot(v1, v2):
  return sum(a * b for a, b in zip(v1, v2))


def intersect_in_area(p_1, v_1, p_2, v_2, low, high):
  Ax2, Ay2 = v_1
  Bx2, By2 = v_2
  determinant = Ax2 * -By2 + Bx2 * Ay2
  if determinant == 0: return False

  dist = [b - a for a, b in zip(p_1, p_2)]
  d1 = dot([-By2, Bx2], dist) / determinant
  d2 = dot([-Ay2, Ax2], dist) / determinant
  if d1 < 0 or d2 < 0: return False
  
  location = [x + d1 * v for x, v in zip(p_1, v_1)]
  return all(a >= low and a <= high for a in location)


def solve(p, low, high):
  stones = [(stone[:2], stone[3:5]) for stone in p]
  part1 = sum(intersect_in_area(*a, *b, low, high) for a, b in itertools.combinations(stones, 2))
  return part1


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day24.txt"),200e12,400e12)}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
