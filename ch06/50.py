import pandas as pd
df = pd.read_csv("NewsAggregatorDataset/newsCorpora.csv", sep="\t", header=None, index_col=None,
                 names=["ID", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"])
df

select = ["Reuters", "Huffington Post",
          "Businessweek", "Contactmusic.com", "Daily Mail"]

df = df[df["PUBLISHER"].isin(select)]
df = df.sample(frac=1, random_state=0)

train = len(df)*8/10
val = len(df)/10

train_data = df.iloc[:int(train), [4, 1]]
train_data.to_csv("train.txt", header=None, index=None, sep="\t")
print("train.txt:", len(train_data))

validation_data = df.iloc[int(train):int(train+val), [4, 1]]
validation_data.to_csv("validation.txt", header=None, index=None, sep="\t")
print("validation.txt:", len(validation_data))

test_data = df.iloc[int(train+val):, [4, 1]]
test_data.to_csv("test.txt", header=None, index=None, sep="\t")
print("test.txt:", len(test_data))
