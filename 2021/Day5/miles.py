from helpers import *
import re

def part1(filename: str) -> int:
  lines = to_lines(filename)
  d={}
  for line in lines:
    match = "([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)"
    x1, y1, x2, y2 = [int(x) for x in re.match(match, line).groups()]
    print(x1,y1,x2,y2)
    if x1 == x2:
      print("x1=x2", x1)
      for y in range(y1,y2+1):
        if not (x1,y) in d:
          d[(x1,y)] = 0
        d[(x1,y)] += 1
    elif y1 == y2:
      print("y1=y2", y1)
      for x in range(x1,x2+1):
        print(f'bumping ({x}{y1})')
        if not (x,y1) in d:
          d[(x,y1)] = 0
        d[(x,y1)] += 1

  print(d)
  # print({k: v for k, v in d.items() if v>1})

  ret = len({k: v for k, v in d.items() if v>1})
  return ret



def part2(filename: str) -> int:
  pass #TODO: complete
