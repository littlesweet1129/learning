#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 23:29:36 2018

@author: Teresa
"""

tup = 4,5,6
tup
nested_tup = (4,5,6), (7,8)
nested_tup
tuple([4,0,2])
tup = tuple('string')
tup
tup[0]
tup = tuple(['foo', [1,2], True])
tup[2] = False # tuple is immutable
tup[1].append(3) # mutable object inside the tuple can be modified in place
tup
(4, None,'foo')+(6,0)+('bar', )
('foo', 'bar')*4

tup = (4,5,6)
a,b,c = tup
b
tup = 4,5,(6,7)
a,b,(c,d) = tup
d
a, b = 1, 2
a, b = b, a # swap variabe names
a
seq = [(1,2,3), (4,5,6), (7,8,9)]
for a,b,c in seq:
    print('a={0}, b={1}, c={2}'.format(a,b,c))
values = 1,2,3,4,5
a,b,*rest = values
a, b    
rest # rest can be any arbitrary variable name

a = (1,2,2,2,3,4,2)
a.count(2) # count number of occurrance of a value

a_list = [2,3,7,None]
tup = ('foo', 'bar', 'baz')
b_list = list(tup)
b_list
b_list[1] = 'peekaboo' # list is mutable
b_list
gen = range(10)
gen
list(gen)
b_list.append('dwarf')
b_list
b_list.insert(1,'red') # insert is computationally expensive compared to append
b_list
b_list.pop(2)
b_list
b_list.append('foo')
b_list
b_list.remove('foo')
'dwarf' in b_list
'dwarf' not in b_list
[4, None, 'foo'] + [7,8,(2,3)] # concatenation by addition is a comparatively expensive operation since a new list must be created and 
x = [4, None, 'foo']
x.extend([7,8,(2,3)]) # append and pop is only one element in the list, extend is adding another list
x

everything = []
for chunk in list_of_lists:
    everything.extend(chunk)
# is faster than
everything = []
for chunk in list_of_lists:
    everything = everything + chunk
    
a = [7,2,5,1,3]
a.sort() # sort the list in-place
a
b = ['saw', 'small', 'He', 'foxes', 'six']
b.sort(key=len)
b
import bisect # bisect module does not check whether the list is sorted
c=[1,2,2,2,3,4,7]
bisect.bisect(c,2) # bisect finds the location where the element should be inserted to keep it sorted
bisect.bisect(c,5)
bisect.insort(c,6)
c

seq = [7,2,3,7,5,6,0,1]
seq[2:5]
seq[3:4] = [6,3]
seq
seq[:5]
seq[3:]
seq[-4:]
seq[-6:-2]
seq[::2]
seq[::-1]

for i,value in enumerate(collection):
    # do something with value
    
some_list = ['foo', 'bar', 'baz']     
mapping = {}
for i,v in enumerate(some_list):
    mapping[v] = i
mapping    
sorted([7, 1, 2, 6, 0, 3, 2])
sorted('horse race')
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zipped = zip(seq1, seq2)
zipped
list(zipped)
seq3 = [False, True]
list(zip(seq1, seq2, seq3)) # zip can take an arbitrary number of sequences, and drive bu the shortest
for i, (a,b) in enumerate(zip(seq1, seq2)):
    print('{0}: {1}, {2}'.format(i, a, b))
pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
first_names, last_names = zip(*pitchers)
first_names
last_names
list(reversed(range(10)))

empty_dict = {}
d1 = {'a' : 'some value', 'b' : [1, 2, 3, 4]}
d1
d1[7] = 'an integer'
d1
d1['b']
'b' in d1
d1[5] = 'some value'
d1
d1['dummy'] = 'another value'
d1
del d1[5]
d1
ret = d1.pop('dummy')
ret
d1
list(d1.keys())
list(d1.values())
d1.update({'b' : 'foo', 'c' : 12})
d1
mapping = {}
for key,value = zip(key_list, value_list):
    mapping[key] = value
mapping = dict(zip(range(5), reversed(range(5))))
mapping
value = some_dict.get(key, default_value)
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter=word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
by_letter
for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)
by_letter

from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
by_letter
hash('string') # check hashability
hash((1,2,(2,3)))
hash((1,2,[2,3])) # fails because lists are mutable
d = {}
d[tuple([1,2,3])] = 5
d[[1,2,3]]=5

set([2,2,2,1,3,3]) # set is an unordered collection of unique elements
{2,2,2,1,3,3}
a={1,2,3,4,5}
b={3,4,5,6,7,8}
a.union(b)
a|b
a.intersection(b)
a&b
a.issubset(b)
a.issuperset(b)
a.isdisjoint(b)
c = a.copy()
c |= b
c
d = a.copy()
d &= b
d
my_data = [1, 2, 3, 4]
my_set = {tuple(my_data)}
my_set
{1,2,3} == {3,2,1}
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
[x.upper() for x in strings if len(x)>2]
unique_lengths = {len(x) for x in strings}
unique_lengths
set(map(len, strings))
loc_mapping = {val: index for index,val in enumerate(strings)}
loc_mapping
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
result = [name for names in all_data for name in names if name.count('e')>=2]
result
some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]
flattened
[[x for x in tup] for tup in some_tuples]

def my_function(x,y,z=1.5):
    if z>1:
        return z*(x+y)
    else:
        return z/(x+y)
    
a = None

def bind_a_variable():
#    global a
    a=[]
a
bind_a_variable()
print(a)
def f(): 
    a=5 
    b=6 
    c=7
    return a, b, c
a,b,c=f()
a
states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south   carolina##', 'West virginia?']
import re
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result
clean_strings(states)
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)
clean_ops = [str.strip, remove_punctuation, str.title]
def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result
clean_strings(states, clean_ops)
for x in map(remove_punctuation,states):
    print(x)

def short_function(x):
    return x*2
equiv_anon = lambda x: x*2
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key=lambda x:len(set(list(x))))
strings

def add_numbers(x,y):
    return x+y
add_five = lambda y: add_numbers(5, y)
add_five(2)
from functools import partial
add_five = partial(add_numbers, 5)
add_five(7)

some_dict = {'a': 1, 'b': 2, 'c': 3}
for key in some_dict:
    print(key)
dict_iterator = iter(some_dict)
dict_iterator
list(dict_iterator)

def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n**2))
    for i in range(1, n+1):
        yield i**2
gen = squares()
gen
for x in gen:
    print(x, end=' ')
    
gen = (x**2 for x in range(100))
gen
sum(x**2 for x in range(100))
dict((i, i**2) for i in range(5))
dict((a,b) for a,b in enumerate(range(10)))

import itertools
first_letters = lambda x: x[0]
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
for letter, names in itertools.groupby(names, first_letters):
    print(letter, list(names))
itertools.combinations(range(5), 4)
float('1.2345')
float('something')
def attempt_float(x):
    try: 
        return float(x)
    except:
        return x
attempt_float('1.2345')
attempt_float('something')
attempt_float((1,2))
float((1,2))
def attempt_float(x):
    try:
        return float(x)
    except ValueError:
        return x
attempt_float((1,2))
attempt_float('something')

def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x
attempt_float('1.2345')
attempt_float('something')
f = open(path, 'w')
try:
    write_to_file(f)
finally:
    f.close()
    
try:
    write_to_file(f)
except:
    print('Failed')
else:
    print('Succeeded')
finally:
    f.close()
    
path = '../examples/segismundo.txt'
f = open(path)
for line in f:
    pass
lines = [x.rstrip() for x in open(path)]
lines
f.close()
with open(path) as f:
    lines = [x.rstrip() for x in f]
lines
# this will automatically close the filw when existing the with block    
f = open(path)
print(f.read(10), f.read(10).encode('utf-8'))
f2 = open(path, 'rb')
print(f2.read(10), f2.read(10).decode())
# .read keeps reading the number of bytes while the file handle's position keep moving forward

f.tell() # .tell gives the current position of the handle
f2.tell()
import sys
sys.getdefaultencoding()
f.seek(3) # .seek change the handle positio to the indicated byte in file
f.tell()
f.read(1)
f.close()
f2.close()

with open('tmp.txt', 'w') as handle:
    handle.writelines(x for x in open(path) if len(x) > 1)
with open('tmp.txt') as f:
    lines = f.readlines()
lines
