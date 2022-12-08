from helpers import *

def part1(filename: str) -> int:
  t = to_lines(filename)
  g =  int(''.join("1" if ith_sum(t,i) >= len(t)//2 else "0" for i in range(len(t[0]))), 2)
  return g*(2**len(t[0])-g-1)

def part2(filename: str) -> int:
  t = to_lines(filename)
  a=b=""

  for i in range(len(t[0])):
    aa = [l for l in t if l.startswith(a)]
    bb = [l for l in t if l.startswith(b)]
    a += aa[0][i] if len(aa)==1 else ("1" if ith_sum(aa,i) >= len(aa)/2 else "0")
    b += bb[0][i] if len(bb)==1 else ("0" if ith_sum(bb,i) >= len(bb)/2 else "1")
  return int(a,2)*int(b,2)

def ith_sum(lines, i):
  return sum(int(x[i]) for x in lines)