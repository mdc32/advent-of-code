from helpers import *

def part1(filename: str) -> int:
  s = 0
  l = to_lines(filename)
  for i in l:
    n = [c for c in i if c.isnumeric()]
    s += int(n[0]+n[-1])
  return s

def part2(filename: str) -> int:
  pass #TODO: complete
