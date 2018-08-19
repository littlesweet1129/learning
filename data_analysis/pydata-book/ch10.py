#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:57:19 2018

@author: Teresa
"""

df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})
df
grouped = df.data1.groupby(df.key1)
grouped
grouped.mean()
means = df.data1.groupby([df.key1, df.key2]).mean()
means
dd = df.set_index(['key1', 'key2'])
dd.mean(level=[0,1])
means.unstack()
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
df.data1.groupby([states,years]).mean()
df.groupby('key1').mean()
df.groupby(['key1','key2']).mean()
df.groupby(['key1','key2']).size() # number of rows
df.groupby(['key1','key2']).count() # size include nan, count does not, count is applied column wise
df
df.groupby(['key1','key2']).size().unstack()
# any missing values in a group key will be excluded from the result
for name, group in df.groupby('key1'):
    print(name)
    print(group)
for (k1, k2), group in df.groupby(['key1', 'key2']):
    print((k1, k2))
    print(group)
# groupby generates a sequence of 2-tuples containing the group name and the sbset of data
pieces = dict(list(df.groupby('key1')))
pieces['a']
df.dtypes
grouped = df.groupby(df.dtypes, axis=1) # groupby the columns
for dtype, group in grouped:
    print(dtype)
    print(group)
df.groupby('key1').data1
df.groupby('key1')[['data2']]
df.data1.groupby(df.key1)
df[['data2']].groupby(df.key1)
df.groupby(['key1', 'key2']).data2.mean()
s_grouped = df.groupby(['key1', 'key2']).data2
s_grouped
people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
people.iloc[2:3, [1,2]] = np.nan
people
mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f' : 'orange'}
mapping
by_column = people.groupby(mapping, axis=1)
by_column.sum()
map_series = pd.Series(mapping)
map_series
people.groupby(map_series, axis=1).count()
people.groupby(len).sum()
key_list = ['one', 'one', 'one', 'two', 'two']
people.groupby([len, key_list]).min() # key_list is used with name as index
people
columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                     [1, 3, 5, 1, 3]],
                                     names=['cty', 'tenor'])
columns
hier_df = pd.DataFrame(np.random.randn(4, 5), columns=columns)
for name, group in hier_df.groupby(level='cty', axis=1):
    print(name)
    print(group)
hier_df.groupby(level='cty', axis=1).count()
df
grouped = df.groupby('key1')
grouped.data1.quantile(0.9)
def peak_to_peak(arr):
    return arr.max()-arr.min()
grouped.agg(peak_to_peak)
grouped.describe()
tips = pd.read_csv('../examples/tips.csv')
tips.head()
tips['tip_pct'] = tips.tip/(tips.total_bill-tips.tip)
grouped = tips.groupby(['day', 'smoker'])
grouped_pct = grouped['tip_pct']
grouped_pct.agg('mean')
grouped_pct.mean()
grouped_pct.agg(['mean','std',peak_to_peak])
grouped_pct.agg([('foo', 'mean'), ('bar', np.std)]) # give column names to the aggregation result
functions = ['count', 'mean', 'max']
result = grouped['tip_pct', 'total_bill'].agg(functions)
result
result['tip_pct']
ftuples = [('Durchschnitt', 'mean'), ('Abweichung', np.var)]
grouped['tip_pct', 'total_bill'].agg(ftuples)
grouped.agg({'tip': np.max, 'size': 'sum'})
grouped.agg({'tip': [('max', np.max)], 'size': [('sum', 'sum')]})
grouped.agg({'tip_pct': ['min', 'max', 'mean', 'std'], 'size': 'sum'})
tips.groupby(['day', 'smoker'], as_index=False).mean()
tips.groupby(['day', 'smoker']).mean().reset_index() # using as_index=False avoids some unnecessary computations
def top(df, n=5, column='tip_pct'):
    return df.sort_values(by=column)[-n:]
top(tips, n=6)
tips.groupby('smoker').apply(top)
tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill')
tips.groupby(['smoker', 'day']).total_bill.agg('max')
# function inside apply needs to return a pandas object or a scalar value
result = tips.groupby('smoker')['tip_pct'].describe()
result.stack()
result.unstack('smoker')
f = lambda x: x.describe()
tips.groupby('smoker')['tip_pct'].apply(f)
tips.groupby('smoker', group_keys=False).apply(top)
tips.groupby('smoker', as_index=False).apply(top)
tips.groupby('smoker').apply(top)
frame = pd.DataFrame({'data1': np.random.randn(1000),
                      'data2': np.random.randn(1000)})
quartiles = pd.cut(frame.data1, 4)
quartiles.head()
def get_stats(group):
    return {'min': group.min(),
            'max': group.max(),
            'count': group.count(),
            'mean': group.mean()}
grouped = frame.data2.groupby(quartiles)
grouped.apply(get_stats).unstack()
grouping = pd.qcut(frame.data1, 10, labels=False)
grouping
grouped = frame.data2.groupby(grouping)
grouped.apply(get_stats).unstack()
s = pd.Series(np.random.randn(6))
s[::2] = np.nan
s
s.fillna(s.mean())
states = ['Ohio', 'New York', 'Vermont', 'Florida',
          'Oregon', 'Nevada', 'California', 'Idaho']
group_key = ['East']*4+['West']*4
data = pd.Series(np.random.randn(8), index=states)
data
data[['Vermont', 'Nevada', 'Idaho']]=np.nan
data
data.groupby(group_key).mean()
fill_mean = lambda g: g.fillna(g.mean()) 
data.groupby(group_key).apply(fill_mean)
fill_values = {'East': 0.5, 'West': -1}
fill_func = lambda g: g.fillna(fill_values[g.name])
data.groupby(group_key).apply(fill_func)
dd = pd.concat([data.reset_index(), pd.Series(data.values), pd.Series(group_key)], axis=1)
dd.columns=['state', 'a', 'b', 'key']
dd
dd.groupby('key').apply(fill_mean)
suits = ['H', 'S', 'C', 'D']
card_val = (list(range(1, 11))+[10]*3)*4
base_names = ['A']+list(range(2, 11))+['J', 'K', 'Q']
len(base_names)
card_val
cards = []
for suit in suits:
    cards.extend(str(num)+suit for num in base_names)
deck = pd.Series(card_val, index=cards)
deck[:13]
def draw(deck, n=5):
    return deck.sample(n)
draw(deck)
get_suit = lambda card: card[-1]
deck.groupby(get_suit).apply(draw, n=2)
deck.groupby(get_suit, group_keys=False).apply(draw, n=2)
df = pd.DataFrame({'category': ['a', 'a', 'a', 'a',
                                'b', 'b', 'b', 'b'],
                   'data': np.random.randn(8),
                   'weights': np.random.rand(8)})
df       
grouped = df.groupby('category')
get_wavg = lambda g: np.average(g.data,weights=g.weights)
grouped.apply(get_wavg)
!head -10 ../examples/stock_px_2.csv
close_px = pd.read_csv('../examples/stock_px_2.csv', parse_dates=True, index_col=0)
close_px.info()
close_px.isnull().mean()
spx_corr = lambda x: x.corrwith(x.SPX) # x is the dataframe
rets = close_px.pct_change().dropna()
rets.head()
get_year = lambda x: x.year
by_year = rets.groupby(get_year)
by_year.apply(spx_corr)
by_year.apply(lambda g: g.AAPL.corr(g.MSFT))
import statsmodels.api as sm
def regress(data, yvar, xvars):
    Y=data[yvar]
    X=data[xvars]
    X['intercept']=1
    result = sm.OLS(Y, X).fit()
    return result.params
by_year.apply(regress, 'AAPL', ['SPX'])
tips.head()
tips.pivot_table(index=['day', 'smoker']) # by default, it computes a table of group means
tips.groupby(['day', 'smoker']).mean()
tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker')
# computes mean size and tip_pct for combination of time, day and smoker
tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker', margins=True)
tips.pivot_table(['tip_pct'], index=['time', 'smoker'], columns='day', aggfunc=len, margins=True)
tips.pivot_table(['tip_pct'], index=['time', 'size', 'smoker'], columns='day', aggfunc='mean', fill_value=0)
#cross-tabulation is a special case of a pivot table that computes group frequencies
data = pd.DataFrame({'Sample': range(1, 11),
                     'Nationality': ['USA', 'Japan']*2+['Japan']*2+['USA']*2+['Japan', 'USA'],
                     'Handedness': ['Right-handed', 'Left-handed', 'Right-handed']*3+['Right-handed']})
data
pd.crosstab(data.Nationality, data.Handedness, margins=True)
pd.crosstab([tips.time, tips.day], tips.smoker, margins=True)
