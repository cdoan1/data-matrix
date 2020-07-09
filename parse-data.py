import pandas as pd

df = pd.read_csv("./version-v-tested.csv")

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

sorting = df.sort_values(by=['release'], ascending=False)
print(df.head())
print(sorting.head())

release43 = df[df['release'].str.contains("4.3")].sort_values(by=['release'], ascending=False)
print(release43.head())