from helpers import *
import re
reg = "move ([0-9]+) from ([0-9]) to ([0-9])"

def part1(filename: str) -> int:
  s, rl = parse_input(filename)
  for l in rl:
    n,a,b = [int(x) for x in re.match(reg,l).groups()]
    for i in range(n):
      s[b-1].append(s[a-1].pop())
  return ''.join(x[-1] for x in s)

def part2(filename: str) -> int:
  s, rl = parse_input(filename)
  for l in rl:
    n,a,b = [int(x) for x in re.match(reg,l).groups()]
    t = s[a-1][-n:]
    s[a-1] = s[a-1][:-n]
    s[b-1] = s[b-1]+t
  return ''.join(x[-1] for x in s)


def parse_input(filename):
  lines = to_lines(filename, nostrip=True)
  sl = lines[:lines.index("\n")-1]
  rl = lines[lines.index("\n")+1:]
  s = [[] for i in range(len(sl[0])//4)]
  for l in sl:
    for i in range(len(s)):
      if l[i*4+1] != " ":
        s[i] = [l[i*4+1]]+s[i]
  return s, rl