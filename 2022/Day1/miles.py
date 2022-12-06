from helpers import *

def part1(filename: str) -> int:
  return sorted([sum(c) for c in to_int_chunks(filename)])[-1]

def part2(filename: str) -> int:
  return sum(sorted([sum(c) for c in to_int_chunks(filename)])[-3:])

