import time, re, math


def load(file):
  with open(file) as f:
    return [re.findall('%?&?\w+',row) for row in f.readlines()]
  

def build_modules(p):
  modules = dict()
  for sender, *receiver in p:
    name, type = sender[1:], sender[0]
    match type:
      case '%': state = False
      case '&': state = dict()
      case 'b': state = None
    modules[name] = [name, type, receiver, state]
  for sender,_,receiver,_ in modules.values():
    for rec in receiver:
      if rec not in modules: continue
      if modules[rec][TYPE] != '&': continue
      modules[rec][STATE][sender] = False
  return modules


def solve(p):
  modules = build_modules(p)
  BC = 'roadcaster'
  LowHigh = [0,0]
  main_conjunction = [module[SENDER] for module in modules.values() if 'rx' in module[RECEIVER]][0]
  cycle = {sender:0 for sender in modules[main_conjunction][STATE]}
  for button in range(1,10_000):
    if all(cycle.values()): break
    fifo = [('Button', BC, False)]
    while fifo:
      sender, receiver, impulse = fifo.pop(0)
      if button < 1001: LowHigh[impulse] += 1
      if receiver not in modules: continue
      
      if receiver == main_conjunction and impulse:
        cycle[sender] = button - cycle[sender]  
      
      if modules[receiver][TYPE] == '%':
        if impulse: continue
        modules[receiver][STATE] = not modules[receiver][STATE]
        impulse = modules[receiver][STATE]
      
      if modules[receiver][TYPE] == '&':
        modules[receiver][STATE][sender] = impulse
        impulse = not all(modules[receiver][STATE].values())
      
      for nxt in modules[receiver][RECEIVER]:
        fifo.append((receiver,nxt,impulse))
  
  return math.prod(LowHigh), math.lcm(*cycle.values())
  

time_start = time.perf_counter()
SENDER, TYPE, RECEIVER, STATE = range(4)
print(f'Part 1: {solve(load("day20.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')