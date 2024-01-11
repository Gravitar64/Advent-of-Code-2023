import time, re, collections, math


def load(file):
  with open(file) as f:
    return [re.findall('%?&?\w+', row) for row in f]


def solve(p):
  TYPE, RECEIVERS, STATE = range(3)
  modules, modules_i = dict(), collections.defaultdict(set)
  for sender, *receivers in p:
    type, sender = sender[0], sender[1:]
    modules[sender] = [type, receivers, False]
    for receiver in receivers:
      modules_i[receiver].add(sender)
  for receiver, senders in modules_i.items():
    if receiver not in modules: continue
    if modules[receiver][TYPE] != '&': continue
    modules[receiver][STATE] = {s: False for s in senders}

  lowHigh = [0, 0]
  master_conjunction = modules_i['rx'].pop()
  cycles = dict()

  for button in range(1, 10_000):
    fifo = [('button', 'roadcaster', False)]
    while fifo:
      sender, receiver, pulse = fifo.pop(0)
      if button < 1001:
        lowHigh[pulse] += 1
      if receiver not in modules: continue

      if receiver == master_conjunction and pulse:
        cycles[sender] = button - cycles.get(sender, 0)

      if modules[receiver][TYPE] == '%':
        if pulse: continue
        pulse = modules[receiver][STATE] = not modules[receiver][STATE]

      if modules[receiver][TYPE] == '&':
        modules[receiver][STATE][sender] = pulse
        pulse = not all(modules[receiver][STATE].values())

      for nxt in modules[receiver][RECEIVERS]:
        fifo.append((receiver, nxt, pulse))

  return math.prod(lowHigh), math.lcm(*cycles.values())


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day20.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')