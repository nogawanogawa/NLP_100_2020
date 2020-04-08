import pandas as pd

filename = "popular-names.txt"
df = pd.read_csv(filename, header=None, sep="\t")

print(df.sort_values(2, ascending=False))
