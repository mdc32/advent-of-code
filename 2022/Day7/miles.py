from helpers import *

def part1(filename: str) -> int:
  s = parse(filename)
  l = (size(x) for x in ngen(s))
  return sum(x for x in l if x < 100000)

def part2(filename: str) -> int:
  s = parse(filename)
  k = size(s)
  l = (size(x) for x in ngen(s))
  return min(x for x in l if k-x<=40000000)

def parse(filename):
  s = {"/": {}}
  p = []
  with open(filename) as file:
    cmd = file.readline().strip()
    while cmd:
      if cmd.startswith("$ cd"):
        cd = cmd[5:]
        if cd == "..":
          p = p[:-1]
        else:
          p.append(cd)
        cmd = file.readline().strip()
      elif cmd.startswith("$ ls"):
        wd = nget(s,p)
        while True:
          f = file.readline().split()
          if not f: return s
          if f[0] == "$": 
            cmd = ' '.join(f)
            break
          elif f[0] == "dir" and not f[1] in wd:
            wd[f[1]] = {}
          else: wd[f[1]] = int(f[0])
  return s

def nget(d,k):
  if len(k) == 1:
    return d[k[0]]
  return nget(d[k[0]], k[1:])

def size(d):
  return d if type(d) == int else sum(size(c) for c in d.values())

def ngen(d):
  for k,v in d.items():
    if type(v) == dict:
      yield v
      yield from ngen(v)