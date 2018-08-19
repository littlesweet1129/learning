#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 14:28:16 2018

@author: Teresa
"""

path = '../datasets/bitly_usagov/example.txt'
!head -5 ../datasets/bitly_usagov/example.txt
open(path).readline()
import json
records = [json.loads(line) for line in open(path)]
records[0]
import pandas as pd
records_dd = pd.read_json(path, lines=True)
records_dd.head()
time_zones = [rec['tz'] for rec in records]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
time_zones[:10]
def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts
get_counts(time_zones)
from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x]+=1
    return counts
counts = get_counts2(time_zones)
counts['America/New_York']
len(time_zones)
def top_counts(count_dict, n=10):
    value_key_pair = [(count, tz) for tz, count in count_dict.items()]
    value_key_pair.sort()
    return value_key_pair[-n:]
top_counts(counts)

from collections import Counter
counts = Counter(time_zones)
counts.most_common(10)

import pandas as pd
records[:2]
frame = pd.DataFrame(records)
frame.head()
frame.info()
frame.tz[:10]
tz_counts = frame.tz.value_counts()
tz_counts[:10]
clean_tz = frame.tz.fillna('Missing')
clean_tz[clean_tz==''] = 'Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:10]
import seaborn as sns
subset = tz_counts[:10]
sns.barplot(y=subset.index, x=subset.values)
frame['a'][1]
frame['a'][50]
frame['a'][51][:50]
results = pd.Series([x.split()[0] for x in frame.a.dropna()])
results[:5]
results.value_counts()[:8]
cframe = frame[frame.a.notnull()]
import numpy as np
cframe['os'] = np.where(cframe.a.str.contains('Windows'), 'Windows', 'Not Windows')
cframe.os[:5]
by_tz_os = cframe.groupby(['tz', 'os'])
agg_counts = by_tz_os.size().unstack().fillna(0)
agg_counts[:10]
indexer = agg_counts.sum(1).argsort()
indexer[:10]
count_subset = agg_counts.take(indexer[-10:])
count_subset
agg_counts.sum(1).nlargest(10)
count_subset = count_subset.stack()
count_subset
count_subset.name='total'
count_subset = count_subset.reset_index()
count_subset[:10]
sns.barplot(x='total', y='tz', hue='os', data=count_subset)
def norm_total(group):
    group['normed_total'] = group.total/group.total.sum()
    return group
results = count_subset.groupby('tz').apply(norm_total)
results.head()
sns.barplot(x='normed_total', y='tz', hue='os', data=results)
g = count_subset.groupby('tz')
results2 = count_subset.total/g.total.transform('sum')

!head -5 ../datasets/movielens/users.dat
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('../datasets/movielens/users.dat', sep='::', header=None, names=unames)
users.head()
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('../datasets/movielens/ratings.dat', sep='::', header=None, names=rnames)
ratings.head()
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('../datasets/movielens/movies.dat', sep='::', header=None, names=mnames)
movies.head()
data = pd.merge(pd.merge(ratings, users), movies)
data.head()
data.iloc[0]
mean_ratings = data.pivot_table('rating', 
                                index = 'title',
                                columns='gender', 
                                aggfunc='mean')

dd = mean_ratings[:5].stack()
dd.head()
dd.columns

sns.barplot(x='mean_rating', y='title', hue='gender', data=dd)
