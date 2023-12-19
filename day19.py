import time
import collections
import math
import copy


def load(file):
  with open(file) as f:
    return f.read()


def comb(rule_dict, cur_rule='in', ranges=dict(x=(1, 4000), m=(1, 4000), a=(1, 4000), s=(1, 4000))):
  if cur_rule == 'R':
    return 0

  if cur_rule == 'A':
    return math.prod(high - low + 1 for low, high in ranges.values())

  total = 0

  for condition in rule_dict[cur_rule]:
    if ':' in condition:
      con, target = condition.split(':')
      var, op, val = con[0], con[1], int(con[2:])
      low, high = ranges[var]
      if val < low or val > high: continue
      
      if op == '>':
        ranges[var] = (val + 1, high)
        total += comb(rule_dict, target, copy.deepcopy(ranges))
        ranges[var] = (low, val)
      else:
        ranges[var] = (low, val - 1)
        total += comb(rule_dict, target, copy.deepcopy(ranges))
        ranges[var] = (val, high)
   
    else:
      total += comb(rule_dict, condition, copy.deepcopy(ranges))

  return total


def solve(p):
  rule_dict = collections.defaultdict(list)
  rules, xmas = [[row for row in e.split('\n')] for e in p.split('\n\n')]

  for rule in rules:
    name, conditions = rule.split('{')
    conditions = conditions[:-1]
    for condition in conditions.split(','):
      rule_dict[name].append(condition)

  xmas = [eval(f'dict({s[1:-1]})') for s in xmas]

  part1, start_rule = 0, 'in'
  for part in xmas:
    cur_rule = start_rule
    while True:
      for condition in rule_dict[cur_rule]:
        if ':' in condition:
          con, target = condition.split(':')
          if eval(f'{part[con[0]]}{con[1:]}'):
            cur_rule = target
            break
        else:
          cur_rule = condition
          break

      if cur_rule == 'A':
        part1 += sum(part.values())
        break

      if cur_rule == 'R':
        break

  part2 = comb(rule_dict)
  return part1, part2


time_start = time.perf_counter()
print(f'Part 1&2: {solve(load("day19.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
