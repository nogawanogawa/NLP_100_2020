import pandas as pd

df = pd.read_csv("neko.txt.mecab", header=None, sep='\t|,', usecols=[
                 0, 1, 2, 7], names=['surface', 'pos', 'pos1', 'base'], skiprows=4, skipfooter=1)

df_new = df[df["surface"] != "EOS"]

df = df_new[df["pos"] == "動詞"]
print(set(df["base"].to_list()))
