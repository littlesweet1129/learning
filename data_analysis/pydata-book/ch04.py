#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 19:56:42 2018

@author: Teresa
"""

import numpy as np
np.random.seed(12345)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(10,6))
np.set_printoptions(precision=4, suppress=True)
my_arr = np.arange(1000000)
my_arr
my_list = list(range(1000000))
my_list
%timeit my_arr2 = my_arr*2
%timeit my_list2 = [x*2 for x in my_list]

data = np.random.randn(2,3)
data
data*10
data+data
data.shape
data.dtype
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
arr1
data2 = [[1,2,3,4], [5,6,7,8]]
arr2 = np.array(data2)
arr2
arr2.ndim
arr2.shape
arr1.dtype
arr2.dtype
np.zeros(10)
np.zeros((3,6))
np.empty((2,3,2))
np.arange(15)

arr = np.array([[1.,2.,3.], [4.,5.,6.]])
arr
arr*arr
arr-arr
1/arr
arr**0.5
arr2 = np.array([[0.,4.,1.], [7.,2.,12.]])
arr2
arr2>arr
arr = np.arange(10)
arr
arr[5]
arr[5:8]
arr[5:8]=12
arr
arr[:]=64
arr
arr2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
arr2d[0][2]
arr2d[0,2]
%timeit arr2d[0][2]
%timeit arr2d[0,2]

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7,4)
names
data
names !='Bob'
data[~(names=='Bob')]
data[names !='Bob']
arr = np.empty((8,4))
for i in range(8):
    arr[i]=i
arr
arr[[4,3,0,6]]
arr[[-3, -5, -7]]
arr = np.arange(32).reshape(8,4)
arr
arr[[1,5,7,2], [0,3,1,2]]
arr[[1,5,7,2]][:,[0,3,1,2]]

arr = np.random.randn(7)*5
arr
remainder, whole_part = np.modf(arr)
whole_part
np.sqrt(arr)
np.sqrt(arr, arr)
arr
points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
ys
z=np.sqrt(xs**2+ys**2)
z
xs.shape
z.shape
xs

x = np.array([[1.,2.,3,], [4.,5.,6.]])
x@ np.ones(3)
x.dot(np.ones(3))
from random import normalvariate
N=1000000
%timeit samples = [normalvariate(0,1) for _ in range(N)]
%timeit np.random.normal(size=N)
np.random.seed(1234)
np.random.randn(1)
rng = np.random.RandomState(1234)
rng.randn(10)
