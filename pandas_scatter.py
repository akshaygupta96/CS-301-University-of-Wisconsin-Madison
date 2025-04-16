#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:11:03 2017

@author: alexi
"""
import numpy as np
import pandas as pd

#1. Make a NumPy array of values
data = np.random.rand(100,2)

#2. Convert to a Pandas DataFrame
df = pd.DataFrame(data,columns=["x axis","y"])
#print df

#3 Plot the data
#Types of plots we've seen:
#scatter
#bar
#box (requires more data formatting)
#hist
axes = df.plot(kind='scatter',x="x axis",y="y",title="Title Here",
               color="Red", label="Data set 1") #If we stop here, Anaconda/Spyder will display in the builtin console

#4 Get a figure from the axes
#fig = axes.get_figure()

#5 Save it!
#fig.savefig("random_scatter.png")