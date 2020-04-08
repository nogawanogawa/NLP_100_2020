import pandas as pd

filename = "popular-names.txt"
df = pd.read_csv(filename, header=None, sep="\t")

print(df.groupby(0, as_index=False).count().sort_values(1, ascending=False))
