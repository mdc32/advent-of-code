from helpers import *
from functools import reduce


def part1(filename: str) -> int:
  lines = [list(map(int, list(x))) for x in to_lines(filename)]
  l = len(lines[0])
  print([mcv([x[i:i+1] for x in lines]) for i in range(l)])
  v = int(''.join([str(mcv([x[i:i+1] for x in lines])) for i in range(l)]),2)
  return v* (2**l-v-1)



def part2(filename: str) -> int:
  lines = to_lines(filename)

def mcv(lines):
  return 1 if sum([int(x[0]) for x in lines]) >= len(lines)/2 else 0

def lcv(lines):
  return 0 if sum([int(x[0]) for x in lines]) >= len(lines)/2 else 1