from helpers import *
s = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part1(filename: str) -> int:
  lines = to_lines(filename)
  def score(l):
    h1,h2 = set(l[:len(l)//2]),set(l[len(l)//2:])
    return s.index(h1.intersection(h2).pop())
  return sum([score(l) for l in lines])

def part2(filename: str) -> int:
  l = to_lines(filename)
  x=0
  for i in range(0,len(l),3):
    b = set(l[i]).intersection(set(l[i+1])).intersection(set(l[i+2]))
    x+=s.index(b.pop())
  return x
