import time, re, collections, math


def load(file):
  with open(file) as f:
    return [re.findall('%?&?\w+', row) for row in f]
  

def solve(p):
  TYPE, RECEIVER, STATE = range(3)
  modules, modules_i = dict(), collections.defaultdict(set)
  for sender, *receiver in p:
    type, sender = sender[0], sender[1:]
    match type:
      case '%': state = False
      case '&': state = dict()
      case 'b': state = None
    modules[sender] = [type, receiver, state]
    for rec in receiver:
      modules_i[rec].add(sender)
  
  for rec, senders in modules_i.items():
    if rec not in modules: continue
    if modules[rec][TYPE] != '&': continue
    modules[rec][STATE] = {s:False for s in senders}
  
  master_conjunction = modules_i['rx'].pop()
  cycles = dict()
  
  lowHigh = [0,0]
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

      for nxt in modules[receiver][RECEIVER]:
        fifo.append((receiver, nxt, pulse))
  return math.prod(lowHigh), math.lcm(*cycles.values())        










  return modules
       
     


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day20.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')