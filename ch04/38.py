import pandas as pd
import japanize_matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv("neko.txt.mecab", header=None, sep='\t|,', usecols=[
                 0, 1, 2, 7], names=['surface', 'pos', 'pos1', 'base'], skiprows=4, skipfooter=1)

words = df["base"]
sr = pd.Series(words)
counts = sr.value_counts()
a = pd.DataFrame(counts).reset_index()
a = a.set_index("index")
a.hist(column="base", bins=400, figsize=(15, 3))
plt.show()
