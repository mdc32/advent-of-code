from helpers import *
import numpy as np

def part1(filename: str) -> int:
  g = np.array([[int(c) for c in l] for l in to_lines(filename)])
  w,h = len(g[0]), len(g)
  m1 = np.array([f(l) for l in g])
  m2 = np.array([f(l) for l in g.T]).T
  m3 = np.fliplr(np.array([f(l) for l in np.fliplr(g)]))
  m4 = np.flipud(np.array([f(l) for l in np.flipud(g).T]).T)
  return np.sum(1 - m1*m2*m3*m4)
  

def part2(filename: str) -> int:
  g = np.array([[int(c) for c in l] for l in to_lines(filename)])
  w,h = len(g[0]), len(g)
  m1 = np.array([v(l) for l in g])
  m2 = np.array([v(l) for l in g.T]).T
  m3 = np.fliplr(np.array([v(l) for l in np.fliplr(g)]))
  m4 = np.flipud(np.array([v(l) for l in np.flipud(g).T]).T)
  return np.amax(m1*m2*m3*m4)


def f(l):
  m = [1]*len(l)
  h = -1
  for i in range(len(l)):
    if l[i] > h:
      h = l[i]
      m[i] = 0
  return m

def v(l):
  m = [0]*len(l)
  for i in range(1,len(l)):
    k = i-1
    while l[k]<l[i] and k>0:
      k -= m[k]
    m[i] = i-k
  return m
    
