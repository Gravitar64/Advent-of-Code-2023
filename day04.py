import time


def load(file):
  with open(file) as f:
    return [row.strip()[row.index(':')+1:].split('|') for row in f]
  

def solve(p):
  part1 = 0
  card_amounts = [1] * len(p)
  for card_no, (winning, have) in enumerate(p):
    winning = set(map(int,winning.split()))
    have = set(map(int,have.split()))
    winner = len(winning & have)
    if winner:
      part1 += 2**(winner-1)
      for n in range(1, winner+1):
        card_amounts[card_no+n] += card_amounts[card_no] 
  return part1, sum(card_amounts)     


time_start = time.perf_counter()
print(f'Part 1: {solve(load("day04.txt"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')