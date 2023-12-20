import time, math


def load(file):
  with open(file) as f:
    return [row.strip().split(' -> ') for row in f]
  
class Module():
  def __init__(self,name,type,dest):
    self.name = name
    self.type = type
    self.dest = dest
    match type:
      case '%': self.mem = False
      case '&': self.mem = {}
      case _  : self.mem = None  

  def __repr__(self):
    return f'Name: {self.name} Type: {self.type} Dest: {self.dest} Mem: {self.mem}'
  
  def receive_impulse(self,impulse,last):
    if self.type == '%':
      self.mem = not self.mem
      return self.mem
    
    if self.type == '&':
      self.mem[last] = impulse
      return not all(self.mem.values())

    
def solve(p):
  modules = dict()
  for module, destinations in p:
    curr = [d.strip() for d in destinations.split(',')]
    if module == 'broadcaster':
      modules[module] = Module('broadcaster',None,curr)
    else:
      modules[module[1:]] = Module(module[1:],module[0],curr)
  
  for object in modules.values():
    for dest in object.dest:
      if dest not in modules: continue
      obj2 = modules[dest]
      if obj2.type != '&': continue
      obj2.mem[object.name]=False
  
  part1 = [0,0]
  for n in range(1,1001):
    queue = [(dest,False,'broadcaster') for dest in modules['broadcaster'].dest]
    part1[0] += 1
    while queue:
      curr, impulse, last = queue.pop(0)
      part1[impulse] += 1
      if curr not in modules: continue
      curr = modules[curr]
            
      if curr.type == '%' and impulse: continue
      impulse = curr.receive_impulse(impulse,last)
      
      for nxt in curr.dest:
        queue.append((nxt, impulse, curr.name))


  main_module = [m.name for m in modules.values() if 'rx' in m.dest][0]
  part2 = {m:0 for m in modules[main_module].mem}
  while not all(part2.values()):
    n += 1
    queue = [(dest,False,'broadcaster') for dest in modules['broadcaster'].dest]
    while queue:
      curr, impulse, last = queue.pop(0)
      if curr not in modules: continue
      curr = modules[curr]
            
      if curr.name == main_module and impulse:
        part2[last] = n - part2[last]

      if curr.type == '%' and impulse: continue
      impulse = curr.receive_impulse(impulse,last)
      
      for nxt in curr.dest:
        queue.append((nxt, impulse, curr.name))

  return math.prod(part1), math.lcm(*part2.values())



time_start = time.perf_counter()
print(f'Part 1: {solve(load("day20.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')