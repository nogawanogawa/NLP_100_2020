import pandas as pd
import sys

args = sys.argv
num_chunks = int(args[1])
filename = "popular-names.txt"

df = pd.read_csv(filename, header=None)

rows = int(len(df) / num_chunks)

for i in range(num_chunks-1):
    df_split = df.iloc[i*rows:i*rows+rows-1, :]
    df_split.to_csv("chunk_"+str(i)+".txt", index=None, header=None)

df_split = df.iloc[(num_chunks-1)*rows:, :]
df_split.to_csv("chunk_"+str(num_chunks-1)+".txt", index=None, header=None)
