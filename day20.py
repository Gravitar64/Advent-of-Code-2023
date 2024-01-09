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
    modules[sender] = [type, receiver, state]
    for rec in receiver:
      modules_inv[rec].add(sender)
  
  for rec, sender in modules_inv.items():
    if rec not in modules: continue
    if modules[rec][TYPE] != '&': continue
    modules[rec][STATE]={s:False for s in sender}
    
  master_conjunction = modules_inv['rx'].pop()
  cycle = dict()
     
  lowHigh = [0,0]
  for button in range(10_000):
    fifo = [('Button', 'roadcaster', False)]
    while fifo:
      sender, receiver, impulse = fifo.pop(0)
      if button < 1000: lowHigh[impulse] += 1
      if receiver not in modules: continue

      if receiver == master_conjunction and impulse:
        cycle[sender] = button - cycle.get(sender,0)

      if modules[receiver][TYPE] == '%':
        if impulse: continue
        impulse = modules[receiver][STATE] = not modules[receiver][STATE]
   
      if modules[receiver][TYPE] == '&':
        modules[receiver][STATE][sender] = impulse
        impulse = not all(modules[receiver][STATE].values())

      for receiver_receiver in modules[receiver][RECEIVER]:
        fifo.append((receiver, receiver_receiver, impulse))

  return math.prod(lowHigh), math.lcm(*cycle.values())


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day20.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')