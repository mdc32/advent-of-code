from helpers import *
from functools import reduce


def part1(filename: str) -> int:
  t = [*zip(*[list(n) for n in to_lines(filename)])]
  v = int(''.join([str(mcv(x)) for x in t]),2)
  return v*(2**len(t)-v-1)



def part2(filename: str) -> int:
  lines = to_lines(filename)

def mcv(lines):
  return 1 if sum([int(x[0]) for x in lines]) >= len(lines)/2 else 0

def lcv(lines):
  return 0 if sum([int(x[0]) for x in lines]) >= len(lines)/2 else 1