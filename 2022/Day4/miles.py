from helpers import *
import re
reg = "([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)"

def part1(filename: str) -> int:
  li = to_lines(filename)
  def score(l):
    g = [int(x) for x in re.match(reg,l).groups()]
    if (g[0]<=g[2] and g[1]>=g[3]) or (g[0]>=g[2] and g[1]<=g[3]):
      return 1
    return 0
  return sum(score(l) for l in li)


def part2(filename: str) -> int:
  li = to_lines(filename)
  def score(l):
    g = [int(x) for x in re.match(reg,l).groups()]
    if (g[2]<=g[0]<=g[3]) or (g[0]<=g[2]<=g[1]):
      return 1
    return 0
  return sum(score(l) for l in li)
