import pandas as pd

df = pd.read_csv("popular-names.txt", sep="\t", header=None)

col1 = df.iloc[:, [0]]
col2 = df.iloc[:, [1]]

col1.to_csv("col1.txt", header=None, index=None)
col2.to_csv("col2.txt", header=None, index=None)
