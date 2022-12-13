from helpers import *
opp = "ABC"
me = "XYZ"
s1=[[4,8,3],[1,5,9],[7,2,6]]
s2=[[3,4,8],[1,5,9],[2,6,7]]

def part1(filename: str) -> int:
  p = [l.split() for l in to_lines(filename)]
  return sum(s1[opp.index(o)][me.index(m)] for o,m in p)

def part2(filename: str) -> int:
  p = [l.split() for l in to_lines(filename)]
  return sum(s2[opp.index(o)][me.index(m)] for o,m in p)