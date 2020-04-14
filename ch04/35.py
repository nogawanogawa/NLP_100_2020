import pandas as pd

df = pd.read_csv("neko.txt.mecab", header=None, sep='\t|,', usecols=[
                 0, 1, 2, 7], names=['surface', 'pos', 'pos1', 'base'], skiprows=4, skipfooter=1)

words = df["base"]
sr = pd.Series(words)
counts = sr.value_counts()
a = pd.DataFrame(counts).reset_index()
print(a)
