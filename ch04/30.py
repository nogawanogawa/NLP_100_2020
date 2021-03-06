import pandas as pd

df = pd.read_csv("neko.txt.mecab", header=None, sep='\t|,', usecols=[
                 0, 1, 2, 7], names=['surface', 'pos', 'pos1', 'base'], skiprows=4, skipfooter=1)

df_new = df[df["surface"] != "EOS"]

l = df_new.to_dict(orient='records')

print(l)
