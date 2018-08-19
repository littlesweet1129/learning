#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 13:51:45 2018

@author: Teresa
"""

import pandas as pd
!cat ../examples/ex1.csv
df = pd.read_csv('../examples/ex1.csv')
df
pd.read_table('../examples/ex1.csv', sep=',')
!cat ../examples/ex2.csv
pd.read_csv('../examples/ex1.csv', header=None)
pd.read_csv('../examples/ex1.csv', names=['a', 'b', 'c', 'd', 'message'])
names = ['a', 'b', 'c', 'd', 'message']
pd.read_csv('../examples/ex1.csv', names=names, index_col=4) # or index_col='message'
!cat ../examples/csv_mindex.csv
parsed = pd.read_csv('../examples/csv_mindex.csv', index_col=['key1', 'key2'])
parsed
!cat ../examples/ex3.txt
result = pd.read_table('../examples/ex3.txt', sep='\s+')
result
!cat ../examples/ex4.csv
pd.read_csv('../examples/ex4.csv', skiprows=[0,2,3])
!cat ../examples/ex5.csv
result = pd.read_csv('../examples/ex5.csv')
result
pd.isnull(result)
result.isnull()
pd.read_csv('../examples/ex5.csv', na_values=['Null'])
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
pd.read_csv('../examples/ex5.csv', na_values=sentinels)

pd.options.display.max_rows=10
result = pd.read_csv('../examples/ex6.csv')
result
pd.read_csv('../examples/ex6.csv', nrows=5)
chunker = pd.read_csv('../examples/ex6.csv', chunksize=1000)
chunker
tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece.key.value_counts(), fill_value=0)
tot.sort_values(ascending=False)[:10]
chunker = pd.read_csv('../examples/ex6.csv', iterator=True)
chunker.get_chunk(5)

data = pd.read_csv('../examples/ex5.csv')
data
data.to_csv('../examples/out.csv')
!cat ../examples/out.csv
import sys
data.to_csv(sys.stdout, sep='|') # rwriting to sys.stdout, it prints the test result to the console
data.to_csv(sys.stdout, na_rep='NULL')
data.to_csv(sys.stdout, index=False, header=False)
data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])
dates = pd.date_range('1/1/2000', periods=7)
dates
import numpy as np
ts = pd.Series(np.arange(7), index=dates)
ts.to_csv('../examples/tseries.csv')
!cat ../examples/tseries.csv
!cat ../examples/ex7.csv
import csv
f = open('../examples/ex7.csv')
reader = csv.reader(f)
for line in reader:
    print(line)
f.close()
with open('../examples/ex7.csv') as f:
    lines = list(csv.reader(f))
lines
header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}
data_dict
class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ','
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL
reader = csv.reader(f, dialect = my_dialect)    
reader
for line in reader:
    print(line)
with open('../examples/ex7.csv') as f:
    lines = list(csv.reader(f, dialect = my_dialect))
lines
with open('../examples/mydata.csv', 'w') as f:
    writer = csv.writer(f, dialect=my_dialect)
    writer.writerow(('one', 'two', 'three')) 
    writer.writerow(('1', '2', '3')) 
    writer.writerow(('4', '5', '6')) 
    writer.writerow(('7', '8', '9'))
!cat ../examples/mydata.csv

obj = """
{"name": "Wes",
     "places_lived": ["United States", "Spain", "Germany"],
     "pet": null,
     "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
                  {"name": "Katie", "age": 38,
                   "pets": ["Sixes", "Stache", "Cisco"]}]
}
     """
import json
result = json.loads(obj)
result
asjson = json.dumps(result)
asjson
siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])
siblings
# json objects + json.loads -> python dict + pd.DataFrame -> python dataframe
!cat ../examples/example.json
# default option for pandas.read_json assume that each object in the json array is a row in the table
data = pd.read_json('../examples/example.json')
data
print(data.to_json())
print(data.to_json(orient='records'))

tables = pd.read_html('../examples/fdic_failed_bank_list.html')
len(tables)
type(tables[0])
failures = tables[0]
failures.head()
close_timestamps = pd.to_datetime(failures['Closing Date'])
close_timestamps.dt.year.value_counts().sort_index().plot()

from lxml import objectify
path = '../datasets/mta_perf/Performance_MNR.xml'
!head -n30 ../datasets/mta_perf/Performance_MNR.xml
parsed = objectify.parse(open(path))
root = parsed.getroot()
data = []
skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ',
               'DESIRED_CHANGE', 'DECIMAL_PLACES']
for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)
len(data)            
data[0]
perf = pd.DataFrame(data)
perf.head()
# xml + lxml -> list of python dict + pd.DataFrame -> data frame

from io import StringIO
tag = '<a href="http://www.google.com">Google</a>'
root = objectify.parse(StringIO(tag)).getroot()
root
root.get('href')
root.text

frame = pd.read_csv('../examples/ex1.csv')
frame
frame.to_pickle('../examples/frame_pickle')
pd.read_pickle('../examples/frame_pickle')
frame = pd.DataFrame({'a': np.random.randn(100)})
store = pd.HDFStore('mydata.h5')
store['obj1'] = frame
store['obj1_col'] = frame.a
len(store)
type(store['obj1_col'])
store.put('obj2', frame, format='table')
store.select('obj2', where=['index>=10 and index <=15'])
store.close()
frame.to_hdf('mydata.h5', 'obj3', format='table')
pd.read_hdf('mydata.h5', 'obj3', where=['index<5'])
xlsx = pd.ExcelFile('../examples/ex1.xlsx')
xlsx.sheet_names
pd.read_excel(xlsx,'Sheet1')
# pd.ExcelFile -> excel instance + pd.read_excel -> data frame
frame = pd.read_excel('../examples/ex1.xlsx', 'Sheet1')
frame
writer = pd.ExcelWriter('../examples/ex2.xlsx')
frame.to_excel(writer, 'Sheet1')
writer.save()
frame.to_excel('../examples/ex2.xlsx')

import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
type(resp)
data = resp.json()
type(data)
len(data)
data[0].keys()
data[0]['title']
issues = pd.DataFrame(data,columns=['number', 'title','labels', 'state'])
issues

import sqlite3
query = """
CREATE TABLE test (a VARCHAR(20),
                   b VARCHAR(20),
                   c REAL,
                   d INTEGER);
"""
con = sqlite3.connect('mydata.sqlite')
con
con.execute(query)
con.commit()
data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]
stmt = 'INSERT INTO test VALUES(?, ?, ?, ?)'
con.executemany(stmt, data)
con.commit()
cursor = con.execute('select * from test')
rows = cursor.fetchall()
rows
cursor.description
pd.DataFrame(rows, columns=[x[0] for x in cursor.description])
import sqlalchemy as sqla
db = sqla.create_engine('sqlite:///mydata.sqlite')
pd.read_sql('select * from test', db)
