#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 21:59:30 2018

@author: Teresa
"""

def add_numbers(a,b):
    """
    Add two numbers together
    Returns
    ------
    the_sum : type of arguments
    """
    return a+b
add_numbers?
add_numbers??
import numpy as np
np.*load*?

%run ipython_script_test.py
c
result
%load ipython_script_test.py
%paste
%cpaste
a = np.random.randn(100, 100)
%timeit np.dot(a,a)
%debug?
%pwd
foo = %pwd
foo
%magic
%quickref
%matplotlib
%matplotlib inline

a = [1,2,3]
b = a
a.append(4)
b
def append_element(some_list, element):
    some_list.append(element)
data = [1,2,3]
append_element(data,4)
data

a = 5
b = 4.5
isinstance(a, int)
isinstance(a, (int, float))
isinstance(b, (int, float))
a = 'foo'
getattr(a, 'split')
def isiterable(obj): 
    try:
        iter(obj)
        return True
    except TypeError: # not iterable
        return False
isiterable('a string')
isiterable([1,2,3])
isiterable(5)
x = (1,2,3)
if not isinstance(x, list) and isiterable(x):
    x = list(x)
x    

import some_module
result = some_module.f(5)
pi = some_module.PI
pi

from some_module import f, g, PI
result = g(5, PI)
result

import some_module as sm
from some_module import PI as pi, g as gf
r1 = sm.f(pi)
r2 = gf(6, pi)

a = [1,2,3]
b = a
c = list(a)
a is b # to check if two references refer to the same object
a is not c
a == c
a = None
a is None

a = 5
b = 4
a//b
(a == 5) ^ (a != 5)

a_list = ['foo', 2, [4,5]]
a_list[2] = (3,4)
a_list
a_tuple = (3,5,(4,5))
a_tuple[1] = 'four'

a = 'one way of writing a string'
b = "another way"
c = """
this is a long string that
spans multiple lines
"""
c.count('\n')
a = 'this is a string'
a[10] = 'f'
b = a.replace('string', 'longer string')
b
a
a = 5.6
s = str(a)
s
s = 'python'
list(s)
s[:3]
s = '12\\34'
print(s)
s = r'this\has\no\special\characters'
s
a = 'this is the first half '
b = 'and this is the second half'
a + b
template = '{0:.2f} {1:s} are worth US${2:d}'
template.format(4.5560, 'Argentine Pesos', 1)
val = "español"
val
val_utf8 = val.encode('utf-8')
type(val_utf8)
val_utf8.decode('utf-8')

s = '3.14159'
fval = float(s)
type(fval)
int(fval)
bool(fval)
bool(0)
a = None
a is None
b = 5
b is not None

from datetime import datetime, date, time
dt = datetime(2011, 10, 29, 20, 30, 21)
dt
dt.day
dt.minute
dt.date()
dt.time()
dt.strftime('%m/%d/%Y %H:%M')
dt.strftime('%F')
dt.strftime('%D')
datetime.strptime('20091031', '%Y%m%d')
dt.replace(minute=0, second=0)
dt2 = datetime(2011, 11, 15, 22, 30)
delta = dt2-dt
type(delta)
dt + delta

sequence = [1,2,None, 4, None, 5]
total = 0
for value in sequence:
    if value is None:
        continue
    total+=value

sequence = [1,2,0,4,6,5,2,1]
total_until_5 = 0
for value in sequence:
    if value==5:
        break
    total_until_5+=value
for a, b, c in iterator:
    # do osmething
    
x = 256
total = 0
while x>0:
    if total>500:
        break
    total+=x
    x=x//2
    

if x <0:
    print('negative')
elif x ==0:
    # TODO: put something smart here
    pass
else: print('positive')

range(10)
list(range(10))
list(range(0, 20, 2))
list(range(5, 0, -1))
total = 0
for i in range(100000):
    if i%3 ==0 or i%5 ==0:
        total +=i
        
x = 5
'Non-negative' if x>= 0 else 'Negative'
