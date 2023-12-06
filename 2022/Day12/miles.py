from helpers import *
import numpy as np

def part1(filename: str) -> int:
  g = np.array([[ord(c)-97 for c in l] for l in to_lines(filename)])
  S, E = np.where(g == -14), np.where(g == -28)
  g[S] = 0
  g[E] = 25
  q = list(zip(*S))
  print(q)



def part2(filename: str) -> int:
  pass #TODO: complete
