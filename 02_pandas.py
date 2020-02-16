import numpy as np
import pandas as pd

separator = '\n --- \n'
a = pd.Series([1, 2, 3])
print(a)
print(a.index)
print(a.values)

b = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
b[['a', 'b']] = 0
print(b)
print(b.index)
print(b[['c']])
print(b[b > 0])

c = pd.Series({'a': 1, 'b': 2, 'c': 3})
c.name = 'numbers'
c.index.name = 'letters'
print(c)

print(separator)

adf = pd.DataFrame({
    'country': ['Russia', 'Belarus', 'Ukraine'],
    'population': [143.5, 9.5, 45.5],
    'square': [17125191, 207600, 603628],
})
print(adf)
print(adf.population)
print(type(adf.population))

adf.index = ['RU', 'BY', 'UA']
print(adf)

print(adf.loc['RU'])  # by string mark
print(adf.loc[['RU', 'BY'], 'population'])  # by string mark

print(adf.iloc[0])  # by index
print(adf.iloc[[0, 1], [1]])  # by index

adf_filter = (adf.country == 'Russia')
print(adf[adf_filter])
print(adf[adf.population > 20][['country', 'population']])
print(adf[adf.square > 500_000][['country', 'square']])

adf['density'] = adf['population'] / adf['square'] * 1_000_000
print(adf)

print(adf.drop(['density'], axis=1))  # copy
# adf.drop(['density'], axis='columns', inplace=True) # mutation

print(adf.rename(columns={'country': 'ccc'}))  # copy

# extract (copy) sorted data by field
print(adf.nlargest(2, 'population'))
print(adf.nsmallest(2, 'square'))

print(separator)

# write to file
# adf.to_csv('countries2.csv')

# read file (returns DataFrame)
bdf = pd.read_csv('countries.csv', sep=',')
print(bdf)
print(bdf.shape)  # -> (rows, columns)
print(bdf.shape[0])
print(bdf.columns)
print(bdf.head(1))
print(bdf.tail(1))

# stats
print(bdf.describe())
print(bdf.describe(include=['object']))

# reduce memory
print(bdf.info())
bdf['population'] = bdf['population'].astype('float32')
bdf['square'] = bdf['square'].astype('int32')
print(bdf.info())

# categories
print([(col, bdf[col].unique()) for col in bdf.columns])

# sort
print(bdf.sort_values(by=['population'], ascending=[True]).head(2))

# group
print(bdf.groupby(by='population')['country'].max())

# cross
print(pd.crosstab(bdf['population'], bdf['square']))
print(pd.crosstab(bdf['population'], bdf['square'], normalize=True))

# read with chunks
for chunk in pd.read_csv('countries.csv', sep=',', chunksize=1):
    print(chunk.shape)

# options
# pd.set_option('display.max_columns', 100)
# pd.set_option('display.max_rows', 100)
# pd.set_option('display.pecision', 3)
