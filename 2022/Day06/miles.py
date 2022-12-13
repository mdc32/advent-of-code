from helpers import *

def part1(filename: str) -> int:
  with open(filename) as file:
    s = file.read()
    for i in range(4,len(s)):
      if len(set(s[i-4:i])) == 4:
        print(s.index(s[i-4:i]))
        return i

def part2(filename: str) -> int:
  with open(filename) as file:
    s = file.read()
    for i in range(14,len(s)):
      if len(set(s[i-14:i])) == 14:
        print(s[i-14:i])
        return i