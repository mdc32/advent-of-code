from helpers import *

def part1(filename: str) -> int:
  lines = to_lines(filename)
  d,h=0,0
  for l in lines:
      c,v=l[0],int(l[-1])
      if c=="f":
          h+=v
      else:
          d += v if c=="d" else -v
  return d*h

def part2(filename: str) -> int:
  lines = to_lines(filename)
  a,d,h=0,0,0
  for l in lines:
      c,v=l[0],int(l[-1])
      if c=="f":
          h+=v
          d+=v*a
      else:
          a += v if c=="d" else -v
  return d*h
