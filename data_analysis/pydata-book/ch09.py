#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 15:39:53 2018

@author: Teresa
"""

%matplotlib inline
#%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn
data = np.arange(10)
data
plt.plot(data)
fig = plt.figure()
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
plt.plot(np.random.randn(50).cumsum(), 'k--')
ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30)+3*np.random.randn(30))
fig, axes = plt.subplots(2,3)
axes
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i,j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
fig
fig.subplots_adjust(wspace=0, hspace=0)
fig
axes[1,1].plot(np.arange(30), np.arange(30)+3*np.random.randn(30), 'g--')
axes[0,0].plot(np.arange(30), np.arange(30)+3*np.random.randn(30), linestyle = '--', color='g')
from numpy.random import randn

plt.plot(randn(30).cumsum(), 'ko--')
plt.plot(randn(30).cumsum(), linestyle='--', color='k', marker='o')
data = np.random.randn(30).cumsum()

plt.plot(data, 'k--', label='Default')
plt.plot(data, 'k--', drawstyle='steps-post', label='steps-post')
plt.legend(loc='best')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum())
fig
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],
                            rotation=30, fontsize='small')
fig
ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')
fig
props = {'title': 'My first matplotlib plot',
        'xlabel': 'Stages'}
ax.set(**props)
fig

from numpy.random import randn
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(randn(1000).cumsum(), 'k', label='one') # exclude from legend, pass no label, or label='_nolegend_'
ax.plot(randn(1000).cumsum(), 'k--', label='two')
ax.plot(randn(1000).cumsum(), 'k.', label='three')
ax.legend(loc='best') # plt.legend()
ax.text(1,1,'Hello World!', family='monospace', fontsize=10) # 1,1 is the (x,y) coordinates on the plot
fig
from datetime import datetime
import pandas as pd
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
!head -10 ../examples/spx.csv
data = pd.read_csv('../examples/spx.csv', index_col=0, parse_dates=True)
data.head()
spx = data['SPX']
spx.plot(ax=ax, style='k-')
crisis_data = [(datetime(2007, 10, 11), 'Peak of bull market'),
               (datetime(2008, 3, 12), 'Bear Stearns Fails'),
               (datetime(2008, 9, 15), 'Lehman Bankruptcy')]
for date, label in crisis_data:
    ax.annotate(label, xy=(date, spx.asof(date)+75),
                xytext = (date, spx.asof(date)+225),
                arrowprops=dict(facecolor='black', headwidth=4, width=2, headlength=4),
                horizontalalignment='left',
                verticalalignment='bottom')
ax.set_xlim(['2007-01-01', '2011-01-01'])
ax.set_ylim([600, 1800])
ax.set_title('Important dates in the 2008-2009 financial crisis')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]], color='g', alpha=0.5)
ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)
fig.savefig('figpath.svg') # plt.savefig
fig.savefig('figpath.png', dpi=400, bbox_inches='tight')
from io import BytesIO
buffer = BytesIO()
plt.savefig(buffer)
plot_data = buffer.getvalue()

plt.rc('figure', figsize=(10, 10)) 
# first argument is the component to customize, 
# after that can follow a sequence of keyword rguments indicating the new parameters
font_options = {'family': 'monospace',
                'weight': 'bold',
                'size': 10}
plt.rc('font', **font_options)
data.head()
data.plot()

s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot()
df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),
                  columns=['A', 'B', 'C', 'D'],
                  index=np.arange(0, 100, 10))
df
df.plot(subplots=True)
df.plot()
fig, axes = plt.subplots(2,1)
type(fig)
type(axes)
data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))
data
data.plot.bar(ax=axes[0], color='k', alpha=0.7)
data.plot.barh(ax=axes[1], color='k', alpha=0.7)
fig
df = pd.DataFrame(np.random.rand(6, 4),
                  index=['one', 'two', 'three', 'four', 'five', 'six'],
                  columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
df
df.plot.bar()
df.plot.barh(stacked=True, alpha=0.5)
s = pd.Series([1,1,1,2,2,3,3,3]*3)
s
s.value_counts().plot.bar()
!head -10 ../examples/tips.csv
tips = pd.read_csv('../examples/tips.csv')
tips.head()
party_counts = pd.crosstab(tips['day'], tips['size'])
party_counts
tips.pivot_table(values='time', index='day', columns='size', aggfunc = 'count')
party_counts = party_counts.loc[:, 2:5]
party_counts
party_pcts = party_counts.divide(party_counts.sum(1), axis=0) # same as .div with fillna option
party_pcts
party_pcts.plot.bar()
party_pcts.plot.barh(stacked=True)

import seaborn as sns
tips.head()
tips['tip_pct'] = tips.tip/(tips.total_bill-tips.tip)
sns.barplot(x='tip_pct', y='day', data=tips, orient='h') 
# length of the bar is the average tip_pcts on each day
# black line is the 95% confidence interval
sns.barplot(x='tip_pct', y='day', hue='time', data=tips, orient='h') 
sns.set(style='whitegrid')
tips.tip_pct.plot.hist(bins=50)
tips.tip_pct.hist(bins=50)
tips.tip_pct.plot.density()
tips.tip_pct.plot.kde()
comp1 = np.random.normal(0, 1, size=200)
comp1
comp2 = np.random.normal(10, 2, size=200)
values = pd.Series(np.concatenate([comp1, comp2]))
values
sns.distplot(values, bins=100, color='k') 
# distplot plot both a histogram and a continuour density estimate simulation
macro = pd.read_csv('../examples/macrodata.csv')
macro.head()
data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
data.head()
trans_data = np.log(data).diff().dropna()
trans_data[-5:]
sns.regplot('m1', 'unemp', data=trans_data)
plt.title('Changes in log %s versus log %s' % ('m1', 'unemp'))
sns.pairplot(trans_data, diag_kind='kde', plot_kws={'alpha': 0.2})
sns.factorplot(x='day', y='tip_pct', hue='time', col='smoker',kind='bar', data=tips[tips.tip_pct<1])
sns.factorplot(x='day', y='tip_pct', row='time',col='smoker', kind='bar',data=tips[tips.tip_pct<1])
sns.factorplot(x='tip_pct', y='day', kind='box', data=tips[tips.tip_pct<1])
