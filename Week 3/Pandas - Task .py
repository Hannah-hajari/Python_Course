import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Cars93_missing.csv')

df = df.set_index('Model')

df.loc[df['Weight'] > 3500, 'Weight'] = 3500

print("Columns:", df.columns.tolist())
print("Missing values count:\n", df.isnull().sum())

def swap_columns(dataframe, col1, col2):
    cols = list(dataframe.columns)
    i1, i2 = cols.index(col1), cols.index(col2)
    cols[i1], cols[i2] = cols[i2], cols[i1]
    return dataframe[cols]

df = df.reindex(sorted(df.columns), axis=1)

q_low = df['Weight'].quantile(0.05)
q_high = df['Weight'].quantile(0.95)
df_filtered = df[(df['Weight'] >= q_low) & (df['Weight'] <= q_high)]

mean_weight = df['Weight'].mean()
df['Weight'] = df['Weight'].fillna(mean_weight)

dict1 = {'Car_ID': [1, 2, 3], 'Brand': ['Toyota', 'Honda', 'Ford']}
dict2 = {'Rating': [4.5, 4.2, 4.0]}
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
df_merged = pd.concat([df1, df2], axis=1)

corr_matrix = df.select_dtypes(include=['number']).corr()
print("Correlation Matrix:\n", corr_matrix)