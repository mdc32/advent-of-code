from helpers import *

def part1(filename):
  l = to_ints(filename)
  return sum([1 if l[i]<l[i+1] else 0 for i in range(len(l)-1)])

def part2(filename):
  l = to_ints(filename)
  return sum([1 if l[i]<l[i+3] else 0 for i in range(len(l)-3)])
