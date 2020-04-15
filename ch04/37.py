import pandas as pd
import japanize_matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv("neko.txt.mecab", header=None, sep='\t|,', usecols=[
                 0, 1, 2, 7], names=['surface', 'pos', 'pos1', 'base'], skiprows=4, skipfooter=1)

l = pd.Series()
s = pd.DataFrame()
i = 0

while i < len(df):

    if df.at[i, "surface"] != "。":
        s = s.append(df.loc[i])

    else:
        if len(s["base"].str.contains('猫')) != 0:
            l = l.append(s)
        s = pd.DataFrame()

    i += 1

counts = l["base"].value_counts()
a = pd.DataFrame(counts).reset_index()
a = a[:10]
a = a.set_index("index")
a.plot.bar(y=['base'], figsize=(12, 3), legend=False)
plt.show()
