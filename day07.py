import time


def load(file):
  with open(file) as f:
    return [row.strip().split() for row in f]
  

def get_type(cards,part2):
  amounts = [cards.count(n) for n in range(13)]

  if part2:
    joker = amounts.pop(0)
    amounts[amounts.index(max(amounts))] += joker

  if 5 in amounts: return 6
  if 4 in amounts: return 5
  if 3 in amounts and 2 in amounts: return 4
  if 3 in amounts: return 3
  if amounts.count(2) == 2: return 2
  if 2 in amounts: return 1
  return 0
  


def solve(p, part2=False):
  strength = '23456789TJQKA' if not part2 else 'J23456789TQKA'
  ranking = []
  
  for cards, bid in p:
    cards = [strength.index(c) for c in cards]
    type = get_type(cards,part2)
    ranking.append((type, cards, int(bid)))

  ranking = sorted(ranking)
  return sum(rank * bid for rank, (_, _, bid) in enumerate(ranking,start=1))


time_start = time.perf_counter()
puzzle = load("day07.txt")
print(f'Part 1: {solve(puzzle)}')
print(f'Part 2: {solve(puzzle,True)}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')