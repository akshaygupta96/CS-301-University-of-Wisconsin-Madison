# My name: Akshay Gupta
# Partner: Shreya Gaur

import numpy as np #imports numpy module as np
import pandas as pd #imports pandas module as pd

def line_graph():
    """This function plots a cosine graph and saves it into a file."""
    points = np.arange(0,2*np.pi,1/(10*np.pi)) #defines domain for x
    data = np.cos(points) #defines range for y
    alldata = np.array([points,data]) #creates an array for all x and y values
    alldata = alldata.transpose() #transposes all the x and y values
    #print alldata
    df = pd.DataFrame(alldata,columns=["","0"]) #Converts alldata into a Pandas DataFrame
    #print df
    axes = df.plot(x="",y="0", title="Cosine Approximated at Intervals of 1/(10pi)") #Plots the data and gives a title
    fig = axes.get_figure() #Get a figure from the axes
    fig.savefig("my_line_graph.png") #Save into file

def scatterplot():
    """This function plots 3 scatter plots in 1 graph and saves it into a file."""
    red_xplots=np.array([1,1,4]) #defines red x plots
    red_yplots=np.array([1,3,2]) #defines red y plots
    red_df=pd.DataFrame({"x":red_xplots, "y":red_yplots}) #Converts x and y plots into a Pandas DataFrame
    axes1=red_df.plot.scatter(x="x",y="y",title="Scatter Plot in Three Colors", color="red", label="Red Group") #Plots the data in red, gives a title and creates a label in the legend
    yellow_xplots=np.array([1,2,3,6]) #defines yellow x plots
    yellow_yplots=np.array([4,2,5,2]) #defines yellow y plots
    yellow_df=pd.DataFrame({"x":yellow_xplots, "y":yellow_yplots}) #Converts x and y plots into a Pandas DataFrame
    yellow_df.plot.scatter(x="x",y="y", color="yellow", ax=axes1,label="Yellow Group") #Plots the data in yellow and creates a label in the legend
    blue_xplots=np.array([0,0,1,2,3]) #defines blue x plots
    blue_yplots=np.array([1,5,2,3,4]) #defines blue y plots
    blue_df=pd.DataFrame({"x":blue_xplots, "y":blue_yplots}) #Converts x and y plots into a Pandas DataFrame
    blue_df.plot.scatter(x="x",y="y", color="blue", ax=axes1,label="Blue Group") #Plots the data in blue and creates a label in the legend
    fig = axes1.get_figure() #Get a figure from the axes
    fig.savefig("my_scatter_plot.png") #Save into file
    
def histogram():
    """This function creates a histogram and saves it into a file."""
    np.random.seed(5) #sets the random seed
    data=np.random.normal(0,1,10000) #draws 10000 numbers from a normal distribution
    df=pd.DataFrame({"Random Seed: 5":data}) #Convert to a Pandas DataFrame
    axes=df.plot.hist(bins=100, color="green", title="10,000 Draws from randn Across 100 Bins") #Plots the histogram in green and gives a title
    fig = axes.get_figure() #Get a figure from the axes
    fig.savefig("my_histogram.png") #Save into file
