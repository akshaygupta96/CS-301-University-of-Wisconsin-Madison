#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:58:33 2017

@author: alexi
"""

import numpy as np
import pandas as pd

#1. Make a NumPy array of values
#data = np.random.rand(100,2)
#Goal: Make a sine wave
points = np.arange(-np.pi,np.pi) #xvals
data = np.sin(points) #yvals

alldata = np.array([points,data])
alldata = alldata.transpose()
#print alldata

#2. Convert to a Pandas DataFrame
df = pd.DataFrame(alldata,columns=["x","y"])
print df

#3 Plot the data
axes = df.plot(x="x",y="y") #If we stop here, Anaconda/Spyder will display in the builtin console

#3.5 Plot more data
xvals = np.arange(-np.pi,np.pi,.1)
yvals = np.sin(xvals)
data = np.array([xvals,yvals]).transpose()
df = pd.DataFrame(data,columns=["x","y"])
axes2 = df.plot(x="y",y="x",ax=axes) #Optional param ax to use existing axes

#4 Get a figure from the axes
fig = axes2.get_figure()

#5 Save it!
fig.savefig("random_sine2.png")