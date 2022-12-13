from helpers import *

def part1(filename: str) -> int:
  l = to_lines(filename)
  v = {(0,0)}
  hx,hy,tx,ty = 0,0,0,0
  for i in l:
    d,a = i.split()
    for k in range(int(a)):
      if d=="R":
        hx+=1
      elif d=="L":
        hx-=1
      elif d=="U":
        hy+=1
      else:
        hy-=1
      tx,ty = pull((hx,hy),(tx,ty))
      v.add((tx,ty))
  return len(v)

def part2(filename: str) -> int:
  l = to_lines(filename)
  v = {(0,0)}
  p = [(0,0)]*10
  for i in l:
    d,a = i.split()
    for k in range(int(a)):
      hx,hy = p[0]
      if d=="R":
        hx+=1
      elif d=="L":
        hx-=1
      elif d=="U":
        hy+=1
      else:
        hy-=1
      p[0] = (hx,hy)
      for j in range(1,len(p)):
        p[j] = pull(p[j-1], p[j])
      # grid(p)
      v.add(p[-1])
  return len(v)

def pull(h,t):
  hx,hy = h
  tx,ty = t
  xd,yd = abs(hx-tx), abs(hy-ty)
  if xd == 2:
    tx = (hx+tx)//2
    if yd == 2:
      ty = (hy+ty)//2
    else:
      ty=hy
  elif yd ==2:
    ty = (hy+ty)//2
    tx=hx
  return (tx,ty)

def grid(p):
  maxx = max(i[0] for i in p)
  minx = min(i[0] for i in p)
  maxy = max(i[1] for i in p)
  miny = min(i[1] for i in p)
  dx,dy = maxx-minx+1, maxy-miny+1
  g = ["."*(dx+1)]*(dy+1)
  for i in range(len(p)):
    x,y = p[i]
    g[y] = g[y][:x]+str(i)+g[y][x+1:]

  print("="*10)
  for y in range(dy-1,-1,-1):
    print(g[y])
  print("="*10)


  

