# Drop Unnamed: 0 columns from a Pandas DataFrame in Python 

import pandas as pd

df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 8]],
    columns=['bobby', 'hadz', 'com']
)

print(df)

df.to_csv('data.csv', encoding='utf-8')

df = pd.read_csv('data.csv', sep=',', encoding='utf-8')

print('-' * 50)

print(df)
