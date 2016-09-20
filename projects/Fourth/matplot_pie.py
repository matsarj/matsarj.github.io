
#  NFL Fourth Down Statistics
# 
#In this code, we will examine the play-by-play data from the 2015 NFL season,   
#focusing on the fourth down statistics.

import numpy as np # library for handling arrays
import pandas as pd #library for handling dataframes
import matplotlib.pyplot as plt #library for viewing graphs
from matplotlib.widgets import Slider #this method will allow us to add a slider to our graphs

#We first read in the 2015 NFL play-by-play data and grab: all fourth down plays
data = pd.read_csv('/home/matt/Downloads/nfl.csv')
fourth = data[data['down'] == 4]
fourth = fourth[fourth['PlayType'].isin(['Run', 'Pass', 'Punt', 'Field Goal'])]
yds = 1

#Initialize the plot
fig, ax = plt.subplots()
ax.pie(fourth['PlayType'].value_counts())
plt.legend(fourth['PlayType'].value_counts().index, loc = "best")
plt.title("Fourth Downs By Play Type")

#Draw the slider
axYTG = plt.axes([.2,.08, .65, .08], axisbg = 'white')
sYTG = Slider(axYTG, 'Yards To Go', 1, 40, valinit = 0, valfmt = '%0.0f', color = 'brown')

#This is the function that refreshes the plot with the new slider values
def update(val):
	yds = int(round(val))
	ax.clear()
	ax.pie(fourth[fourth['ydstogo'] == yds]['PlayType'].value_counts(dropna = False))
	ax.legend(fourth[fourth['ydstogo'] == yds]['PlayType'].value_counts().index)
	ax.set_title("Fourth Downs By Play Type")
	fig.canvas.draw()
sYTG.on_changed(update)
plt.show()
