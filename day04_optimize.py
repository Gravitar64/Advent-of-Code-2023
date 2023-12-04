def load(file):
  with open(file) as f:
    return [row.strip().split(':')[1] for row in f]
  

def solve(p):
  part1, cards = 0, [1] * len(p)
  for id, row in enumerate(p):
    if winner := len(set.intersection(*[set(map(int,part.split())) for part in row.split('|')])):
      part1 += 2**(winner-1)
      for n in range(1, winner+1):
        cards[id+n] += cards[id] 
  return part1, sum(cards)     


print(f'Part 1: {solve(load("day04.txt"))}')