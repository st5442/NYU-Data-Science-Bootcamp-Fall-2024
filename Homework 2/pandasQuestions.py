import pandas as pd
import numpy as np

#5. From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

result = []
for i in range(0, len(df), 20):
    row = df.loc[i, ['Manufacturer', 'Model', 'Type']]
    result.append(row)

print(result)

#6. Replace missing values in Min.Price and Max.Price columns with their respective mean.

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

print(df[['Min.Price', 'Max.Price']].head())

df['Min.Price'].fillna(df['Min.Price'].mean())
df['Max.Price'].fillna(df['Max.Price'].mean())

print(df[['Min.Price', 'Max.Price']].head())

#7. How to get the rows of a dataframe with row sum > 100?

df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
print(df)

row_sums = df.sum(axis=1)
result = df[row_sums > 100]

print(result)
