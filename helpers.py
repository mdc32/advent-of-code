from typing import List

def to_lines(filename: str) -> List[str]:
  with open(filename) as file:
    return [x.strip() for x in file.readlines()]

def to_ints(filename: str) -> List[int]:
  with open(filename) as file:
    return [int(x.strip()) for x in file.readlines()]