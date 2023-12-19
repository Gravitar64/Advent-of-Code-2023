import time, collections,  math


def load(file):
  with open(file) as f:
    return f.read()


def parsing(p):
  workflows, ratings = [[row for row in block.split('\n')] for block in p.split('\n\n')]
  workflows2 = collections.defaultdict(list)

  for workflow in workflows:
    name, conditions = workflow.split('{')
    for condition in conditions[:-1].split(','):
      con, target = condition.split(':') if ':' in condition else (None, condition)
      if con: con = (con[0], con[1], int(con[2:]))
      workflows2[name].append((con, target))

  ratings = [eval(f'dict({s[1:-1]})') for s in ratings]
  return workflows2, ratings


def comb(wf, curr='in', ranges={c: (1, 4000) for c in 'xmas'}):
  if curr == 'R': return 0
  if curr == 'A': return math.prod(high - low + 1 for low, high in ranges.values())

  total = 0
  for con, target in wf[curr]:
    if not con:
      total += comb(wf, target, ranges)
    else:
      var, op, val = con
      new_ranges = dict(ranges)
      low, high = ranges[var]

      if op == '<':
        new_ranges[var] = (low, val - 1)
        ranges[var] = (val, high)
      else:
        new_ranges[var] = (val + 1, high)
        ranges[var] = (low, val)
      total += comb(wf, target, new_ranges)

  return total


def solve(p):
  workflows, ratings = parsing(p)
  part1 = 0

  for rating in ratings:
    curr = 'in'
    while True:
      for con, target in workflows[curr]:
        if not con:
          curr = target
          break
        var, op, val = con
        if eval(f'{rating[var]}{op}{val}'):
          curr = target
          break

      if curr == 'A':
        part1 += sum(rating.values())
        break

      if curr == 'R':
        break

  return part1, comb(workflows)


time_start = time.perf_counter()
print(f'Part 1 & 2: {solve(load("day19.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
