import pandas as pd
df = pd.read_csv('Cars93_missing.csv')

df = df.set_index('Model')

print(df.head())