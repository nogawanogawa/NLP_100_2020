import pandas as pd

df = pd.read_csv("neko.txt.mecab", header=None, sep='\t|,', usecols=[
                 0, 1, 2, 7], names=['surface', 'pos', 'pos1', 'base'], skiprows=4, skipfooter=1)

l = []
s = []
i = 0

while i < len(df):

    if df.at[i, "pos"] == "名詞":
        s.append(df.loc[i])

    else:
        if len(s) > 1:
            m = ""
            for j in s:
                m += j["surface"]

            l.append(m)

        s = []

    i += 1

print(l)
