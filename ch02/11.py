import pandas as pd

df = pd.read_csv("popular-names.txt", header=None)
print(df.replace("\t", " ", regex=True))
