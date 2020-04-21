import pandas as pd
import nltk

df = pd.read_csv("train.txt", sep="\t", header=None)
for i,item in df.iterrows():
    tokens = nltk.word_tokenize(str(item[1]))
    df.iloc[i,1] = tokens
df.to_csv("train.feature.txt")

df = pd.read_csv("validation.txt", sep="\t", header=None)
for i,item in df.iterrows():
    tokens = nltk.word_tokenize(str(item[1]))
    df.iloc[i,1] = tokens
df.to_csv("validation.feature.txt")

df = pd.read_csv("test.txt", sep="\t", header=None)
for i,item in df.iterrows():
    tokens = nltk.word_tokenize(str(item[1]))
    df.iloc[i,1] = tokens
df.to_csv("test.feature.txt")

