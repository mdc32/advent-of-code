import importlib
import argparse, sys
from datetime import datetime, timezone, timedelta
if __name__ == "__main__":

  now = datetime.now(tz=timezone(timedelta(hours=-5)))
  # i am lazy and this changes to eastern from pacific
  # day = now.day + (0 if now.hour < 21 else 1)

  # set up command line arguments
  parser=argparse.ArgumentParser()
  parser.add_argument('-n', '--name', default="miles", help="run NAME.py (default = miles)")
  parser.add_argument('-d', '--day', default=now.day, type=int)
  parser.add_argument('-y', '--year', default=now.year, type=int)
  parser.add_argument('-t', '--test', help="run test instead of input",
    action='store_true')
  args=parser.parse_args()

  path = f'{args.year}/Day{args.day:02}/'

  # import module for given day and year, with today (eastern) as default
  module = importlib.import_module(f'{path.replace("/",".")}{args.name}')

  # -t flag is used to run test input, otherwise real input is used
  filename = "test.txt" if args.test else "input.txt"

  # run both parts by default
  print(f'Part 1: {module.part1(path+filename)}')
  print(f'Part 2: {module.part2(path+filename)}')
