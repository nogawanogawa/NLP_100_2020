import pandas as pd

df = pd.read_csv("neko.txt.mecab", header=None, sep='\t|,', usecols=[
                 0, 1, 2, 7], names=['surface', 'pos', 'pos1', 'base'], skiprows=4, skipfooter=1)

for index, row in df.iterrows():
    if (df.at[index, "pos"] == "名詞") and (df.at[index+1, "surface"] == "の") and (df.at[index+2, "pos"] == "名詞"):
        print(df.at[index, "surface"] + df.at[index+1,
                                              "surface"] + df.at[index+2, "surface"])
