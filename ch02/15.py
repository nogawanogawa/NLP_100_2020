import sys
import pandas as pd

args = sys.argv
num_rows = int(args[1])
file_name = args[2]

with open(file_name) as f:
    l_strip = [s.strip() for s in f.readlines()]

rows = len(l_strip)

for i in range(num_rows):
    print(l_strip[rows-num_rows+i])
