from helpers import *

def part1(filename: str) -> int:
  ls = to_lines(filename)
  x,s,c = 1,0,0
  for l in (i.split() for i in ls):
    if l[0] == "noop":
      c += 1
      s += c*x if c%40 == 20 else 0
    elif l[0] == "addx":
      c += 2
      s += c*x if c%40 == 20 else 0
      s += (c-1)*x if c%40 == 21 else 0
      x += int(l[1])
  return s


def part2(filename: str) -> int:
  pass #TODO: complete