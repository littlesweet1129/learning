#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 23:40:38 2018

@author: Teresa
"""

import numpy as np
import pandas as pd
values = pd.Series(['apple', 'orange', 'apple', 'apple']*2)
values
pd.unique(values)
values.unique()
pd.value_counts(values)
values.value_counts()
values = pd.Series([0,1,0,0]*2)
values
dim = pd.Series(['apple', 'orange'])
dim.take(values)
fruits = ['apple', 'orange', 'apple', 'apple'] * 2
N = len(fruits)
df = pd.DataFrame({'fruit': fruits,
                   'basket_id': np.arange(N),
                   'count': np.random.randint(3, 15, size=N),
                   'weight': np.random.uniform(0, 4, size=N)},
                   columns=['basket_id', 'fruit', 'count', 'weight'])
df
type(df.fruit)
df.fruit
fruit_cat = df.fruit.astype('category')
fruit_cat
c = fruit_cat.values
c.categories
c.codes
df.fruit = df.fruit.astype('category')
df.fruit
my_categories = pd.Categorical(['foo', 'bar', 'baz', 'foo', 'bar'])
my_categories
categories = ['foo', 'bar', 'baz']
codes = [0,1,2,0,0,1]
my_cats_2 = pd.Categorical.from_codes(codes, categories)
my_cats_2
ordered_cat = pd.Categorical.from_codes(codes, categories, ordered=True)
ordered_cat
my_cats_2.as_ordered()

np.random.seed(12345)
draws = np.random.randn(1000)
draws[:5]
bins = pd.qcut(draws, 4)
type(bins)
bins = pd.qcut(draws, 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
bins
bins.codes[:10]
bins = pd.Series(bins, name='quartile')
bins
results = pd.Series(draws).groupby(bins).agg(['count', 'min', 'max']).reset_index()
results
results.quartile
N = 10000000
draws = pd.Series(np.random.randn(N))
labels = pd.Series(['foo', 'bar', 'baz', 'qux']*(N//4))
categories = labels.astype('category')
labels.memory_usage()
categories.memory_usage()
%time _=labels.astype('category')
s = pd.Series(['a', 'b', 'c', 'd'] * 2)
cat_s = s.astype('category')
cat_s
cat_s.cat.codes # attribute .cat provides access to categorical method just like .str
cat_s.cat.categories
actual_categories = ['a', 'b', 'c', 'd', 'e']
cat_s2 = cat_s.cat.set_categories(actual_categories)
cat_s2
cat_s.value_counts()
cat_s2.value_counts()
cat_s3 = cat_s[cat_s.isin(['a', 'b'])]
cat_s3
cat_s
cat_s3.cat.remove_unused_categories(inplace=True)
cat_s3.value_counts()
cat_s = pd.Series(['a', 'b', 'c', 'd'] * 2, dtype='category')
cat_s
pd.get_dummies(cat_s)

df = pd.DataFrame({'key': ['a', 'b', 'c'] * 4,
                   'value': np.arange(12.)})
df
g = df.groupby('key').value
g.mean()
g.transform(lambda x: x.mean()) # transform is similar to apply but keeping the shape of the original input
g.transform('mean')
g.transform(lambda x: x*2)
df
g.transform(lambda x: x.rank(ascending=False))
def normalize(x):
    return (x-x.mean())/x.std()
g.transform(normalize)
g.apply(normalize)
normalized = (df.value-g.transform('mean'))/g.transform('std') # unwrapped group operation
normalized

N=15
times = pd.date_range('2-17-05-20 00:00', freq='1min', periods=N)
df = pd.DataFrame({'time': times,
              'value': np.arange(N)})
df
df.set_index('time').resample('5min').count()
df2 = pd.DataFrame({'time': times.repeat(3),
                    'key': np.tile(['a', 'b', 'c'], N),
                    'value': np.arange(N*3.)})
df2[:7]
time_key = pd.Grouper(freq='5min') #TimeGrouper is deprecated, and constraint is time must be the index
resampled = df2.set_index('time').groupby(['key', time_key]).sum()
resampled
resampled.reset_index()

df2 = df.copy()
df2['k'] = v
df2 = df.assign(k=v)
result = df2.assign(col1_demeaned=df2.col1-df2.col2.mean()).groupby('key').col1_demeaned.std()
result = (load_data()
          [lambda x: x.col<0]
          .assign(col1_demeaned = lambda x: x.col1-x.col1.mean())
          .groupby('key')
          .col_meaned.std())
a = f(df, arg1=v1)
b = g(a, v2, arg3=v3)
c = h(b, arg4=v4)
# is equivalent to
result = (df.pipe(f, arg1=v1)
          .pipe(g, v2, arg3=v3)
          .pipe(h, arg4=v4))
g = df.groupby(['key1', 'key2'])
df['col1'] = df.col - g.transform('mean')
def group_demean(df, by, cols):
    result = df.copy()
    g = df.groupby(by)
    for c in cols:
        result[c] = df[c]-g[c].transform('mean')
        return result
result = (df[df.col1<0]
          .pipe(group_demean, ['key1', 'key2'], ['col1']))    

