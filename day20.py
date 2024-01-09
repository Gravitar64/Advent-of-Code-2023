import time, re, math, collections


def load(file):
  with open(file) as f:
    return [re.findall('%?&?\w+',row) for row in f]
  

def solve(p):
  modules, modules_inv = dict(), collections.defaultdict(set)
  TYPE, RECEIVER, STATE = range(3)
  for sender, *receiver in p:
    type, sender = sender[0], sender[1:]
    match type:
      case '%': state = False
      case '&': state = dict()
      case 'b': state = None
    modules[sender] = [type,receiver,state]
    for rec in receiver:
      modules_inv[rec].add(sender)

  for rec, sender in modules_inv.items():
    if rec not in modules: continue
    if modules[rec][TYPE] != '&': continue
    modules[rec][STATE] = {s:False for s in sender}

  lowHigh = [0,0]
  master_conjunction = modules_inv['rx'].pop()
  cycles = dict()
 
  for button in range(1,10_000):
    fifo = [('button', 'roadcaster', False)]
    while fifo:
      sender, receiver, pulse = fifo.pop(0)
      if button < 1001: lowHigh[pulse] += 1
      if receiver not in modules: continue

      if receiver == master_conjunction and pulse:
        cycles[sender] = button - cycles.get(sender,0)
        
      if modules[receiver][TYPE] == '%':
        if pulse: continue
        pulse = modules[receiver][STATE] = not modules[receiver][STATE]

      if modules[receiver][TYPE] == '&':
        modules[receiver][STATE][sender] = pulse
        pulse = not all(modules[receiver][STATE].values())  

      for receiver_receiver in modules[receiver][RECEIVER]:
        fifo.append((receiver, receiver_receiver, pulse))

  return math.prod(lowHigh), math.lcm(*cycles.values())


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day20.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')