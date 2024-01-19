import time, re


def load(file):
  with open(file) as f:
    return f.read().split('\n\n')


def change_seed(seed,converters,low=1):
  for converter in converters:
    for i in range(0, len(converter), 3):
      dest, source, rng = converter[i:i + 3]
      if seed < source or seed > (source + rng - 1): continue
      if low == -1: low = source + rng
      seed = seed - source + dest
      break
  return seed, low  


def solve(p):
  numbers = [list(map(int, re.findall('\d+', part))) for part in p]
  seeds, *converters = numbers
  part1 = part2 = float('inf')

  for seed in seeds:
    seed, _ = change_seed(seed, converters)
    part1 = min(part1, seed)

  pairs = [(a,a+b) for a,b in zip(seeds[::2], seeds[1::2])]
  for low, high in pairs:
    while low < high:
      seed, low = change_seed(low, converters, low=-1)     
      part2 = min(part2, seed)

  return part1, part2


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day05.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
