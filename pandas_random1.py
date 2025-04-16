#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:11:03 2017

@author: alexi
"""
import numpy as np
import pandas as pd

#1. Make a NumPy array of values
data = np.random.rand(100)
#print data

#2. Convert to a Pandas DataFrame
df = pd.DataFrame(data)
#print df

#3 Plot the data
axes = df.plot() #If we stop here, Anaconda/Spyder will display in the builtin console
axes.get_figure().show()
#4 Get a figure from the axes
#fig = axes.get_figure()
#fig.show()
#5 Save it!
#fig.savefig("random1.png")
