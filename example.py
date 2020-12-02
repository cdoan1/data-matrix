import pandas as pd

name_dict = {
            'Name': ['a','b','c','d'],
            'Score': [90,80,95,20]
          }

df = pd.DataFrame(name_dict)
dfT = df.T

dfT.to_csv('file_name.csv', index=False)

print (df)
print (dfT)
