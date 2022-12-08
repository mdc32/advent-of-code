from typing import List

def to_lines(filename: str, nostrip=False) -> List[str]:
  with open(filename) as file:
    return [(x if nostrip else x.strip()) for x in file.readlines()]

def to_ints(filename: str) -> List[int]:
  with open(filename) as file:
    return [int(x.strip()) for x in file.readlines()]

def to_chunks(filename: str) -> List[List[str]]:
  with open(filename) as file:
    return [[x.strip() for x in chunk.split("\n")] for chunk in file.read().split("\n\n")]

def to_int_chunks(filename: str) -> List[List[int]]:
  with open(filename) as file:
    return [[int(x.strip()) for x in chunk.split("\n")] for chunk in file.read().split("\n\n")]
