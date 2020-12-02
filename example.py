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


summary_df = pd.read_csv('summary.csv')

summary_df['R1'] = summary_df['Results']
summary_df['R2'] = summary_df['Results']
summary_df['R3'] = summary_df['Results']
summary_df['R4'] = summary_df['Results']
summary_df['R5'] = summary_df['Results']
summary_df['R6'] = summary_df['Results']
summary_df['R7'] = summary_df['Results']
summary_df['R8'] = summary_df['Results']
summary_df['R9'] = summary_df['Results']
summary_df['R10'] = summary_df['Results']
summary_df['R11'] = summary_df['Results']
summary_df['R12'] = summary_df['Results']
summary_df['R13'] = summary_df['Results']
summary_df['R14'] = summary_df['Results']
summary_df['R15'] = summary_df['Results']
summary_df['R16'] = summary_df['Results']
summary_df['R17'] = summary_df['Results']
summary_df['R18'] = summary_df['Results']
summary_df['R19'] = summary_df['Results']
summary_df['R20'] = summary_df['Results']

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
  print (summary_df)

summary_df.to_csv('summary-wide.csv', index=False) 