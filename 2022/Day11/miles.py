from helpers import *
import re

def part1(filename: str) -> int:
  ls = to_lines(filename)
  ms = [None]*((len(ls)+1)//7)

  for i in range(len(ms)):
    ll = ls[i*7:(i+1)*7]
    it = [int(x) for x in re.split(",|:", ll[1])[1:]]
    o = ll[2][17:]
    t,y,n = int(ll[3][19:]), int(ll[4][25:]), int(ll[5][26:])
  
    ms[i] = Monkey(it,o,t,y,n)
  
  for i in range(20):
    for m in ms:
      its = m.inspect()
      for n, it in its:
        ms[n].items.append(it)

  s = sorted(m.inspections for m in ms)
  return s[-1]*s[-2]

def part2(filename: str) -> int:
  ls = to_lines(filename)
  ms = [None]*((len(ls)+1)//7)
  tt = 1

  for i in range(len(ms)):
    ll = ls[i*7:(i+1)*7]
    it = [int(x) for x in re.split(",|:", ll[1])[1:]]
    o = ll[2][17:]
    t,y,n = int(ll[3][19:]), int(ll[4][25:]), int(ll[5][26:])
    tt *= t

    ms[i] = Monkey(it,o,t,y,n)
  

  for i in range(10000):
    for m in ms:
      its = m.inspect2(tt)
      for n, it in its:
        ms[n].items.append(it)

  s = sorted(m.inspections for m in ms)
  print(s)
  return s[-1]*s[-2]

class Monkey:
  def __init__(self, items, op, t,y,n):
    self.items = items
    self.op = lambda old: eval(op)
    self.test = lambda k: y if k%t == 0 else n
    self.inspections = 0

  def inspect(self):
    ts = []
    for i in self.items:
      i = self.op(i)
      self.inspections += 1
      i //= 3
      ts.append((self.test(i), i))
    self.items = []
    return ts

  def inspect2(self, m):
    ts = []
    for i in self.items:
      i = self.op(i)
      self.inspections += 1
      i %= m
      ts.append((self.test(i), i))
    self.items = []
    return ts


