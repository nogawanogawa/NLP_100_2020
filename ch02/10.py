import pandas as pd

df = pd.read_csv("popular-names.txt", sep="¥t", engine='python')
print(df.shape[0])
