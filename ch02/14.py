import sys
import pandas as pd

args = sys.argv
num_rows = args[1]
file_name = args[2]

with open(file_name) as f:
    l_strip = [s.strip() for s in f.readlines()]

for i in range(int(num_rows)):
    print(l_strip[i])
