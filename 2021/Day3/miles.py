from helpers import *
from functools import reduce


def part1(filename: str) -> int:
  t = [*zip(*[list(n) for n in to_lines(filename)])]
  g = int(''.join([str(mcb(x)) for x in t]),2)
  return g*(2**len(t)-g-1)

def part2(filename: str) -> int:
  lines = to_lines(filename)

  while len(lines) > 1:
    newlines = [line for line in lines if]

def mcb(lines):
  return 1 if sum([int(x[0]) for x in lines]) >= len(lines)/2 else 0

def lcb(lines):
  return 0 if sum([int(x[0]) for x in lines]) >= len(lines)/2 else 1